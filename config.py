import os

class Config:
    SECRET_KEY = 'your-secret-key'   # for WTForms / sessions
    SQLALCHEMY_DATABASE_URI = 'sqlite:///aaryasetu.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

