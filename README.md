
# AaryaSetu 

**Connecting Donors, Institutions & Volunteers — A Digital Bridge for Social Good**

AaryaSetu ("Aarya's Bridge" in Sanskrit) is a multilingual web platform that bridges the gap between donors wanting to help and institutions in need. Volunteers facilitate the logistics, creating a seamless ecosystem for meaningful donations.

---

## What Does It Do?

- **Donors** post available items and fulfill urgent institutional needs
- **Institutions** post resource requirements and accept donations matching their needs
- **Volunteers** manage logistics, track deliveries, and ensure items reach their destination
- **Admins** oversee the platform, monitor metrics, and ensure accountability

Real-time status tracking, email notifications, and role-based dashboards make every transaction transparent and rewarding.

---

## Key Features

✨ **Three-Role Ecosystem**
- Seamless workflows for donors, institutions, and volunteers

🌍 **Multilingual Support**  
- English, Hindi, and Kannada built-in (powered by Babel)

📧 **Smart Notifications**
- Real-time email updates at every stage: dispatch, in-transit, delivery, completion

📊 **Admin Dashboard**
- 6-month donation analytics, user management, and donation tracking

🔐 **Secure Authentication**
- Password hashing with Werkzeug, role-based access control

🗂️ **Flexible Donation Matching**
- Support both direct item offerings and need fulfillment

---

## Stack

- **Language:** Python 3
- **Framework:** Flask + Jinja2 templates
- **Database:** SQLite (SQLAlchemy ORM)
- **Notable Libraries:**
  - `flask-login` – session management & role-based auth
  - `flask-babel` – i18n for 3 languages
  - `flask-mail` – email notifications
  - `werkzeug` – password hashing & security

---

## How It's Organized

```
AaryaSetu/
  app/
    __init__.py        Flask app factory, extensions setup
    models.py          User, Need, AvailableItem, Donation models
    routes.py          All API endpoints (~540 lines)
    i18n.py            Multilingual string dictionaries
    templates/         HTML templates (Jinja2)
    static/            CSS, JS, assets
  config.py            Flask configuration (DB, mail, Babel)
  run.py               Entry point
  requirements.txt     Python dependencies
  babel.cfg            i18n extraction config
```

**Request Flow:**
1. Browser hits `/` → Flask routes dispatcher
2. `routes.py` handles auth (login/register), donation workflows, admin tasks
3. Data flows through SQLAlchemy ORM to SQLite
4. Responses rendered with Jinja2 templates + i18n lookups
5. Email notifications dispatched via Flask-Mail on status changes

---

## How to Run It

### Prerequisites
- Python 3.8+
- `pip` package manager

### Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/Ranyaa-11/AaryaSetu.git
cd AaryaSetu

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure email (optional, for notifications)
# Edit app/__init__.py lines 31–33 with your Gmail credentials

# 5. Run the app
python run.py
```

The app will start at `http://127.0.0.1:5000`.

### First-Time Setup

1. **Create Admin Account**  
   Visit `/admin-setup` and use the passcode: `aaryasetu@admin2026`

2. **Register as Donor, Institution, or Volunteer**  
   Go to `/register` and choose your role

3. **Post & Browse**
   - Donors post items at `/post_item`
   - Institutions post needs at `/post_need`
   - Browse available items at `/browse_items` or needs at `/browse_needs`

---

## Core Workflows

### 💝 Donor → Institution Flow
1. Donor registers and posts an available item
2. Institution browses items and accepts one
3. Donor marks as "Dispatched" → email sent
4. Volunteer (if selected) marks as "In Transit" / "Delivered"
5. Institution confirms receipt → donation marked "Completed"

### 🤝 Institution → Donor Flow
1. Institution posts an urgent need
2. Donor browses and makes an offer
3. Status transitions: Pending → Dispatched → Delivered → Completed
4. Emails notify both parties at each stage

---

## Database Models

```python
User(id, name, email, password_hash, role, address, phone, is_admin)
Need(id, item_name, description, quantity, urgency, status, user_id, created_at)
AvailableItem(id, item_name, description, quantity, status, user_id, created_at)
Donation(id, donor_id, institution_id, need_id, item_id, status, delivery_method, created_at, completed_at)
```

**Status States:** Pending → Dispatched → In Transit → Delivered → Completed (or Cancelled)

---

## Admin Features

- **User Management:** Promote/demote admins, view all users
- **Donation Tracking:** Update statuses, trigger email notifications
- **Analytics:** 6-month donation trends, completion rates
- **This Month Summary:** Active donations, posted items/needs, volunteer deliveries

---

## Multilingual (i18n)

Translations managed in `app/i18n.py`. Supported languages:
- `en` – English (default)
- `hi` – हिन्दी (Hindi)
- `kn` – ಕನ್ನಡ (Kannada)

Switch languages at runtime via `/set_lang/<lang>`.

---

## Email Configuration

To enable donation notifications, update `app/__init__.py` (lines 31–33):

```python
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-app-password'  # Use Gmail App Password
```

If mail is not configured, the app gracefully continues (notifications silently fail).

---

## Error Handling

- 404 – Not Found
- 403 – Forbidden (unauthorized role/action)
- 500 – Server Error

All errors render a clean error page with localized messages.

---

## Contributing

Found a bug or want to add a feature? 
- Issues & PRs welcome!
- Follow PEP 8 style for Python code
- Add i18n strings to `i18n.py` for all user-facing text

---

## License

Open source. Use freely for social impact projects.

---

## Roadmap

🚀 Potential enhancements:
- [ ] WhatsApp/SMS notifications
- [ ] Donation receipts & tax certificates
- [ ] Impact reporting (lives touched, items distributed)
- [ ] Search & filtering for items/needs
- [ ] Donor badge/leaderboard system
- [ ] API for third-party integrations

---

**Built with ❤️ for social good. Every donation changes a life.**
