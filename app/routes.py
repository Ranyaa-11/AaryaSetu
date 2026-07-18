from flask import Blueprint, render_template, redirect, url_for, request, flash, session, abort
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, Need, AvailableItem, Donation
from app import db, mail
from app.i18n import t
from functools import wraps
from datetime import datetime, timedelta
from sqlalchemy import func
import re

bp = Blueprint('main', __name__)

ADMIN_SECRET = "aaryasetu@admin2026"

# ─── Helpers ───────────────────────────────────────────────
def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash(t('admin_required'), 'error')
            return redirect(url_for('main.home'))
        return f(*args, **kwargs)
    return decorated

def send_email(to, subject, body):
    """Send email notification in a background thread — never blocks or crashes the request."""
    import threading
    from flask import current_app

    app_obj = current_app._get_current_object()

    def _send(app_obj, to, subject, body):
        with app_obj.app_context():
            try:
                from flask_mail import Message
                msg = Message(subject, recipients=[to], body=body)
                mail.send(msg)
            except Exception as e:
                app_obj.logger.warning(f"Email send failed: {e}")

    thread = threading.Thread(target=_send, args=(app_obj, to, subject, body))
    thread.daemon = True
    thread.start() # Never crash the app over a notification

def notify_donation_status(donation, new_status):
    """Send email to relevant party when donation status changes."""
    donor = User.query.get(donation.donor_id)
    institution = User.query.get(donation.institution_id)
    item_name = donation.item.item_name if donation.item else (
                donation.need.item_name if donation.need else "Item")

    messages = {
        'Dispatched': (
            institution.email if institution else None,
            f"AaryaSetu: Donation On Its Way",
            f"Hello {institution.name if institution else ''},\n\n"
            f"Good news! {donor.name if donor else 'A donor'} has dispatched '{item_name}' to your institution.\n"
            f"Delivery method: {donation.delivery_method}\n\n"
            f"Log in to AaryaSetu to track the delivery.\n\nThank you!"
        ),
        'In Transit': (
            institution.email if institution else None,
            f"AaryaSetu: Delivery In Transit",
            f"Hello {institution.name if institution else ''},\n\n"
            f"A volunteer has picked up '{item_name}' and is on the way to your institution!\n\n"
            f"Log in to AaryaSetu to track the delivery.\n\nThank you!"
        ),
        'Delivered': (
            institution.email if institution else None,
            f"AaryaSetu: Item Delivered — Please Confirm",
            f"Hello {institution.name if institution else ''},\n\n"
            f"'{item_name}' has been delivered to your institution.\n"
            f"Please log in to AaryaSetu and click 'Confirm Receipt' to complete the donation.\n\nThank you!"
        ),
        'Completed': (
            donor.email if donor else None,
            f"AaryaSetu: Donation Complete! 🎉",
            f"Hello {donor.name if donor else ''},\n\n"
            f"Great news! {institution.name if institution else 'The institution'} has confirmed receipt of '{item_name}'.\n"
            f"Your donation is now complete. Thank you for your generosity!\n\nAaryaSetu Team"
        ),
        'Cancelled': (
            institution.email if institution else None,
            f"AaryaSetu: Donation Cancelled",
            f"Hello {institution.name if institution else ''},\n\n"
            f"Unfortunately, the donation of '{item_name}' has been cancelled by the donor.\n"
            f"You may browse other available items on AaryaSetu.\n\nThank you!"
        ),
    }
    if new_status in messages:
        to, subject, body = messages[new_status]
        if to:
            send_email(to, subject, body)

def validate_email(email):
    return re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', email) is not None

def validate_phone(phone):
    if not phone:
        return True  # optional
    return re.match(r'^[\d\s\+\-\(\)]{7,15}$', phone) is not None

# ─── Language ───────────────────────────────────────────────
@bp.route('/set_lang/<lang>')
def set_lang(lang):
    if lang in ['en', 'hi', 'kn']:
        session['lang'] = lang
    return redirect(request.referrer or url_for('main.home'))

# ─── Home ───────────────────────────────────────────────────
@bp.route('/')
def home():
    return render_template('home.html')

# ─── Auth ───────────────────────────────────────────────────
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')

        if not email or not password:
            flash(t('enter_email_password'), 'error')
            return render_template('login.html')

        if not validate_email(email):
            flash(t('invalid_email'), 'error')
            return render_template('login.html')

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            next_page = request.args.get('next')
            if next_page == 'post_need':
                return redirect(url_for('main.post_need'))
            elif next_page == 'post_item':
                return redirect(url_for('main.post_item'))
            return redirect(url_for('main.dashboard'))

        flash(t('invalid_credentials'), 'error')
    return render_template('login.html')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        role = request.form.get('role', '')
        phone = request.form.get('phone', '').strip()
        address = request.form.get('address', '').strip()

        # Validation
        errors = []
        if not name or len(name) < 2:
            errors.append(t('err_name_min'))
        if not validate_email(email):
            errors.append(t('invalid_email'))
        if len(password) < 8:
            errors.append(t('err_password_min'))
        if role not in ['donor', 'institution', 'volunteer']:
            errors.append(t('err_role'))
        if phone and not validate_phone(phone):
            errors.append(t('err_phone'))

        if errors:
            for e in errors:
                flash(e, 'error')
            return render_template('register.html')

        if User.query.filter_by(email=email).first():
            flash(t('email_registered'), 'error')
            return redirect(url_for('main.login'))

        user = User(name=name, email=email, role=role, address=address, phone=phone)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        send_email(email, 'Welcome to AaryaSetu!',
            f"Hello {name},\n\nWelcome to AaryaSetu! Your account has been created successfully as a {role}.\n\n"
            f"Log in at http://127.0.0.1:5000 to get started.\n\nThank you!")

        flash(t('account_created'))
        return redirect(url_for('main.login'))
    return render_template('register.html')


@bp.route('/admin-setup', methods=['GET', 'POST'])
def admin_setup():
    if request.method == 'POST':
        if request.form.get('passcode') != ADMIN_SECRET:
            flash('Incorrect admin passcode.', 'error')
            return render_template('admin_setup.html')

        email = request.form.get('email', '').strip()
        name = request.form.get('name', '').strip()
        password = request.form.get('password', '')

        errors = []
        if not name:
            errors.append('Name is required.')
        if not validate_email(email):
            errors.append('Valid email required.')
        if len(password) < 8:
            errors.append('Password must be at least 8 characters.')
        if errors:
            for e in errors:
                flash(e, 'error')
            return render_template('admin_setup.html')

        if User.query.filter_by(email=email).first():
            flash('Email already registered.', 'error')
            return render_template('admin_setup.html')

        user = User(name=name, email=email, role='admin',
                    phone=request.form.get('phone', ''),
                    is_admin=True)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Admin account created! Please login.')
        return redirect(url_for('main.login'))
    return render_template('admin_setup.html')


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))

# ─── Profile ────────────────────────────────────────────────
@bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        phone = request.form.get('phone', '').strip()
        address = request.form.get('address', '').strip()

        if not name or len(name) < 2:
            flash(t('err_name_min'), 'error')
            return render_template('profile.html')
        if phone and not validate_phone(phone):
            flash(t('err_phone'), 'error')
            return render_template('profile.html')

        current_user.name = name
        current_user.phone = phone
        current_user.address = address
        db.session.commit()
        flash(t('profile_updated'))
        return redirect(url_for('main.profile'))
    return render_template('profile.html')

# ─── Dashboard ──────────────────────────────────────────────
@bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.is_admin:
        return redirect(url_for('main.admin_dashboard'))
    if current_user.role == 'donor':
        my_donations = Donation.query.filter_by(donor_id=current_user.id).all()
        return render_template('donor_dashboard.html', my_donations=my_donations)
    elif current_user.role == 'institution':
        my_donations = Donation.query.filter_by(institution_id=current_user.id).all()
        return render_template('institution_dashboard.html', my_donations=my_donations)
    elif current_user.role == 'volunteer':
        tasks = Donation.query.filter_by(delivery_method='volunteer').all()
        return render_template('volunteer_dashboard.html', tasks=tasks)
    return redirect(url_for('main.home'))

# ─── Admin ──────────────────────────────────────────────────
@bp.route('/admin')
@login_required
@admin_required
def admin_dashboard():
    users = User.query.all()
    donations = Donation.query.order_by(Donation.created_at.desc()).all()
    items = AvailableItem.query.order_by(AvailableItem.created_at.desc()).all()
    needs = Need.query.order_by(Need.created_at.desc()).all()
    user_map = {u.id: u for u in users}

    # ── Monthly analytics ──
    now = datetime.utcnow()
    months = []
    for i in range(5, -1, -1):
        m = now - timedelta(days=30 * i)
        start = m.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        if m.month == 12:
            end = m.replace(year=m.year+1, month=1, day=1)
        else:
            end = m.replace(month=m.month+1, day=1)
        count = Donation.query.filter(
            Donation.created_at >= start,
            Donation.created_at < end
        ).count()
        completed = Donation.query.filter(
            Donation.created_at >= start,
            Donation.created_at < end,
            Donation.status == 'Completed'
        ).count()
        months.append({
            'label': m.strftime('%b %Y'),
            'total': count,
            'completed': completed
        })

    # ── This month summary ──
    month_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    this_month = {
        'new_users': User.query.filter(User.id > 0,
            # approximate: users registered this month via join date proxy
        ).count(),
        'donations': Donation.query.filter(Donation.created_at >= month_start).count(),
        'completed': Donation.query.filter(
            Donation.created_at >= month_start,
            Donation.status == 'Completed').count(),
        'items_posted': AvailableItem.query.filter(
            AvailableItem.created_at >= month_start).count(),
        'needs_posted': Need.query.filter(
            Need.created_at >= month_start).count(),
        'volunteer_deliveries': Donation.query.filter(
            Donation.created_at >= month_start,
            Donation.delivery_method == 'volunteer').count(),
    }

    stats = {
        'total_users': User.query.count(),
        'donors': User.query.filter_by(role='donor').count(),
        'institutions': User.query.filter_by(role='institution').count(),
        'volunteers': User.query.filter_by(role='volunteer').count(),
        'total_items': AvailableItem.query.count(),
        'total_needs': Need.query.count(),
        'total_donations': Donation.query.count(),
        'completed': Donation.query.filter_by(status='Completed').count(),
        'pending': Donation.query.filter_by(status='Pending').count(),
        'in_transit': Donation.query.filter(
            Donation.status.in_(['In Transit', 'Dispatched', 'Delivered'])).count(),
    }

    return render_template('admin_dashboard.html',
                           users=users, donations=donations,
                           items=items, needs=needs,
                           stats=stats, user_map=user_map,
                           months=months, this_month=this_month)


@bp.route('/admin/donation/<int:donation_id>/status', methods=['POST'])
@login_required
@admin_required
def admin_update_status(donation_id):
    donation = Donation.query.get_or_404(donation_id)
    new_status = request.form.get('status')
    donation.status = new_status
    if new_status == 'Completed':
        donation.completed_at = datetime.utcnow()
    db.session.commit()
    notify_donation_status(donation, new_status)
    flash(t('status_updated', status=new_status))
    return redirect(url_for('main.admin_dashboard'))


@bp.route('/make_admin/<int:user_id>')
@login_required
@admin_required
def make_admin(user_id):
    user = User.query.get_or_404(user_id)
    user.is_admin = True
    db.session.commit()
    flash(f'{user.name} is now an admin!')
    return redirect(url_for('main.admin_dashboard'))


@bp.route('/remove_admin/<int:user_id>')
@login_required
@admin_required
def remove_admin(user_id):
    user = User.query.get_or_404(user_id)
    if user.id == current_user.id:
        flash("You can't remove your own admin rights.", 'error')
        return redirect(url_for('main.admin_dashboard'))
    user.is_admin = False
    db.session.commit()
    flash(f'Admin rights removed from {user.name}.')
    return redirect(url_for('main.admin_dashboard'))

# ─── Donation Status Updates ────────────────────────────────
@bp.route('/donation/<int:donation_id>/update', methods=['POST'])
@login_required
def update_donation_status(donation_id):
    donation = Donation.query.get_or_404(donation_id)
    new_status = request.form.get('status')

    if current_user.id == donation.donor_id and new_status in ['Dispatched', 'Delivered', 'Cancelled']:
        donation.status = new_status
        if new_status == 'Completed':
            donation.completed_at = datetime.utcnow()
        db.session.commit()
        notify_donation_status(donation, new_status)
        flash(t('donation_marked', status=new_status))
    elif current_user.id == donation.institution_id and new_status == 'Completed':
        donation.status = 'Completed'
        donation.completed_at = datetime.utcnow()
        db.session.commit()
        notify_donation_status(donation, 'Completed')
        flash(t('donation_received'))
    elif current_user.role == 'volunteer' and new_status in ['In Transit', 'Delivered']:
        donation.status = new_status
        db.session.commit()
        notify_donation_status(donation, new_status)
        flash(t('status_updated', status=new_status))
    else:
        flash(t('not_authorised'), 'error')

    return redirect(url_for('main.dashboard'))

# ─── Post Need ──────────────────────────────────────────────
@bp.route('/post_need', methods=['GET', 'POST'])
@login_required
def post_need():
    if current_user.role != 'institution':
        flash(t('only_inst_post_need'), 'error')
        return redirect(url_for('main.home'))
    if request.method == 'POST':
        item_name = request.form.get('item_name', '').strip()
        quantity = request.form.get('quantity', '').strip()
        urgency = request.form.get('urgency', '')

        errors = []
        if not item_name or len(item_name) < 2:
            errors.append(t('err_item_name'))
        if not quantity.isdigit() or int(quantity) < 1:
            errors.append(t('err_quantity'))
        if urgency not in ['Low', 'Medium', 'High', 'Urgent']:
            errors.append(t('err_urgency'))
        if errors:
            for e in errors:
                flash(e, 'error')
            return render_template('post_need.html')

        need = Need(item_name=item_name,
                    description=request.form.get('description', '').strip(),
                    quantity=int(quantity), urgency=urgency,
                    user_id=current_user.id)
        db.session.add(need)
        db.session.commit()
        flash(t('need_posted'))
        return redirect(url_for('main.browse_needs'))
    return render_template('post_need.html')

# ─── Post Item ──────────────────────────────────────────────
@bp.route('/post_item', methods=['GET', 'POST'])
@login_required
def post_item():
    if current_user.role != 'donor':
        flash(t('only_donor_post_item'), 'error')
        return redirect(url_for('main.home'))
    if request.method == 'POST':
        item_name = request.form.get('item_name', '').strip()
        quantity = request.form.get('quantity', '').strip()

        errors = []
        if not item_name or len(item_name) < 2:
            errors.append(t('err_item_name'))
        if not quantity.isdigit() or int(quantity) < 1:
            errors.append(t('err_quantity'))
        if errors:
            for e in errors:
                flash(e, 'error')
            return render_template('post_item.html')

        item = AvailableItem(item_name=item_name,
                             description=request.form.get('description', '').strip(),
                             quantity=int(quantity), user_id=current_user.id)
        db.session.add(item)
        db.session.commit()
        flash(t('item_posted'))
        return redirect(url_for('main.browse_items'))
    return render_template('post_item.html')

# ─── Browse ─────────────────────────────────────────────────
@bp.route('/browse_needs')
def browse_needs():
    needs = Need.query.filter_by(status='Pending').order_by(Need.created_at.desc()).all()
    return render_template('browse_needs.html', needs=needs)

@bp.route('/browse_items')
def browse_items():
    items = AvailableItem.query.order_by(AvailableItem.created_at.desc()).all()
    return render_template('browse_items.html', items=items)

# ─── Offer / Accept ─────────────────────────────────────────
@bp.route('/offer_need/<int:need_id>', methods=['GET', 'POST'])
@login_required
def offer_need(need_id):
    if current_user.role != 'donor':
        flash(t('only_donor_offer'), 'error')
        return redirect(url_for('main.browse_needs'))
    need = Need.query.get_or_404(need_id)
    if need.status == 'Accepted':
        flash(t('need_fulfilled'), 'error')
        return redirect(url_for('main.browse_needs'))
    if request.method == 'POST':
        donation = Donation(donor_id=current_user.id, institution_id=need.user_id,
                            need_id=need.id,
                            delivery_method=request.form.get('delivery_method'),
                            status='Pending')
        need.status = 'Accepted'
        db.session.add(donation)
        db.session.commit()
        notify_donation_status(donation, 'Dispatched')  # notify institution a donor is coming
        flash(t('offer_thanks'))
        return redirect(url_for('main.dashboard'))
    return render_template('offer.html', need=need)


@bp.route('/accept_item/<int:item_id>', methods=['GET', 'POST'])
@login_required
def accept_item(item_id):
    if current_user.role != 'institution':
        flash(t('only_inst_accept_item'), 'error')
        return redirect(url_for('main.browse_items'))
    item = AvailableItem.query.get_or_404(item_id)
    if item.status == 'Accepted':
        flash(t('item_already_accepted'), 'error')
        return redirect(url_for('main.browse_items'))
    if request.method == 'POST':
        donation = Donation(donor_id=item.user_id, institution_id=current_user.id,
                            item_id=item.id,
                            delivery_method=request.form.get('delivery_method'),
                            status='Pending')
        item.status = 'Accepted'
        db.session.add(donation)
        db.session.commit()
        flash(t('item_accepted'))
        return redirect(url_for('main.dashboard'))
    return render_template('accept.html', item=item)

# ─── Error handlers ─────────────────────────────────────────
@bp.app_errorhandler(404)
def not_found(e):
    return render_template('error.html', code=404, message=t('err_404')), 404

@bp.app_errorhandler(403)
def forbidden(e):
    return render_template('error.html', code=403, message=t('err_403')), 403

@bp.app_errorhandler(500)
def server_error(e):
    return render_template('error.html', code=500, message=t('err_500')), 500
@bp.route('/reset-db-once', methods=['GET', 'POST'])
def reset_db_once():
    if request.method == 'POST':
        if request.form.get('passcode') != ADMIN_SECRET:
            flash('Incorrect passcode.', 'error')
            return '''<form method="POST">
                <input type="password" name="passcode" placeholder="Passcode">
                <button type="submit">Reset Database</button>
            </form>'''
        db.drop_all()
        db.create_all()
        return "<h2>Database reset complete. Remove this route now.</h2>"
    return '''<form method="POST">
        <input type="password" name="passcode" placeholder="Passcode">
        <button type="submit">Reset Database</button>
    </form>'''