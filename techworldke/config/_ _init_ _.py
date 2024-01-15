# config/__init__.py
# Leave this file empty

# config/development.py
class DevelopmentConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SECRET_KEY = 'your_secret_key'
