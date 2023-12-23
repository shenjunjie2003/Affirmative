from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:030129happyjjday@localhost/Affirmative'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + dbusername + ':' + dbpassword + '@localhost/' + dbname
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from affirmative_app import routes
from affirmative_app import models
from affirmative_app import views