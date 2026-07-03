from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_babel import Babel
from flask_mail import Mail

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'main.login'
babel = Babel()
mail = Mail()

def get_locale():
    return session.get('lang', 'en')

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'aaryasetu-secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aaryasetu.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Babel config
    app.config['BABEL_DEFAULT_LOCALE'] = 'en'
    app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'hi', 'kn']

    # Mail config — fill in your Gmail credentials
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'your-email@gmail.com'      # ← change this
    app.config['MAIL_PASSWORD'] = 'your-app-password'          # ← change this
    app.config['MAIL_DEFAULT_SENDER'] = 'AaryaSetu <your-email@gmail.com>'

    db.init_app(app)
    login_manager.init_app(app)
    babel.init_app(app, locale_selector=get_locale)
    mail.init_app(app)

    from app import routes
    app.register_blueprint(routes.bp)

    from app.i18n import t, t_status, LANG_LABELS, SUPPORTED

    @app.context_processor
    def inject_i18n():
        return dict(
            t=t,
            t_status=t_status,
            current_lang=get_locale(),
            lang_labels=LANG_LABELS,
            supported_langs=SUPPORTED,
        )

    with app.app_context():
        db.create_all()

    return app
