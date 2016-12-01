# coding: utf-8
import os


class Config(object):
    """Base config class."""
    # Flask app config
    DEBUG = False
    TESTING = False
    SECRET_KEY = "\xb5\xb3}#\xb7A\xcac\x9d0\xb6\x0f\x80z\x97\x00\x1e\xc0\xb8+\xe9)\xf0}"
    PERMANENT_SESSION_LIFETIME = 3600 * 24 * 7
    SESSION_COOKIE_NAME = 'app_session'

    # Root path of project
    PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # Site domain
    SITE_TITLE = "app"
    SITE_DOMAIN = "http://localhost:5000"

    # SQLAlchemy config
    # See:
    # https://pythonhosted.org/Flask-SQLAlchemy/config.html#connection-uri-format
    # http://docs.sqlalchemy.org/en/rel_0_9/core/engines.html#database-urls
    SQLALCHEMY_DATABASE_URI = "sqlite:////home/narnik/Программы/FlaskProjects/luminate/db/production.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-DebugToolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # Sentry config
    SENTRY_DSN = ''

    # Host string, used by fabric
    HOST_STRING = "root@185.87.193.188"
    
    # Flask_mail configuration
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'narnikgamarnikus@gmail.com'  ## CHANGE THIS
    MAIL_PASSWORD = 'nikogdanesdavatsa'

    # Telegram_bot
    TOKEN = '285591958:AAF5tUpkm1vay_tuV9wwBEPFtC-OPgUJLVI'

