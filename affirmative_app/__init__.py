from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from .config import *
import os

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:030129happyjjday@localhost/Affirmative'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + dbusername + ':' + dbpassword + '@localhost/' + dbname
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'affirmative_app', 'static', 'uploads')
app.config['SESSION_COOKIE_DOMAIN'] = 'affirmative-b9753633e8e0.herokuapp.com'
app.config['SESSION_COOKIE_PATH'] = '/'
app.config['SESSION_COOKIE_NAME'] = 'session'
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SECURE'] = True  # Use True for HTTPS
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # or 'None' if necessary
# app.config['SECRET_KEY'] = os.urandom(24)

app.config.from_object(Config)


db = SQLAlchemy(app)

from affirmative_app import routes
from affirmative_app import models
from affirmative_app import views