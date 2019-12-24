import os

from sayhello import app

dev_db = 'sql:///' + os.path.join(os.path.dirname(app.root_path), 'data.db')

SECRET_KEY = os.getenv('SECRET_KEY', 'aoIEMC3V4B5Q56PsASDFsdf2fVJO.WEF')

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABSE_URI', dev_db)