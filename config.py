import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgres://postgres:djurdjica@localhost:5432/db'
# 'SQLALCHEMY_TRACK_MODIFICATIONS' = False
# SECRET_KEY = os.urandom(32)
# app.config['SECRET_KEY'] = SECRET_KEY # implemented to fix this bug: KeyError: 'A secret key is required to use CSRF.' 
# app.config['WTF_CSRF_SECRET_KEY'] = "secretkey" # same here: secret key - Error

