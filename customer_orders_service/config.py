import os
from dotenv import load_dotenv

load_dotenv()

class ApplicationConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    GOOGLE_CLIENT_ID = os.environ.get('OAUTH_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.environ.get('OAUTH_CLIENT_SECRET')
    GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"
    AT_USERNAME = os.environ.get('AT_USERNAME')
    AT_API_KEY = os.environ.get('AT_API_KEY')


class TestingConfig:
    TESTING = True
    SECRET_KEY = os.environ.get('SECRET_KEY_TEST', 'testing')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI_TEST', 'postgresql://postgres:admin@database:5432/test_db')
    GOOGLE_CLIENT_ID = ''
    GOOGLE_CLIENT_SECRET = ''
    GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"
    AT_USERNAME = os.environ.get('AT_USERNAME')
    AT_API_KEY = os.environ.get('AT_API_KEY')