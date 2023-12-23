"""
routes.py
This file contains the routes for the application.
"""

from . import app
from .views import *

#app.add_url_rule('/', 'index', index, methods=['GET'])
app.add_url_rule('/login', 'login', login, methods=['GET'])

