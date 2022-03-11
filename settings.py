from dotenv import load_dotenv
import os

load_dotenv()


class Config(object):
    SECRET_KEY = str(os.getenv('SECRET_KEY'))
    SQLALCHEMY_DATABASE_URI = str(os.getenv('SQLALCHEMY_DB_URI'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
