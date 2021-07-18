import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secretkey123456789'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///site.db'
    PASSWORD = os.environ.get('ADMIN_PASSWORD' ) or 'password'
    EMAIL = os.environ.get('ADMIN_EMAIL') or 'admin@email.com'