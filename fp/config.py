import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    PASSWORD = os.environ.get('ADMIN_PASSWORD')
    EMAIL = os.environ.get('ADMIN_EMAIL')