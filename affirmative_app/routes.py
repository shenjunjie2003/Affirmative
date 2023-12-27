"""
routes.py
This file contains the routes for the application.
"""

from . import app
from .views import *

app.add_url_rule('/test_db', 'test_db', test_db_connection, methods=['GET'])
app.add_url_rule('/login', 'login', login, methods=['GET'])
app.add_url_rule('/register', 'register', register, methods=['GET', 'POST'])
app.add_url_rule('/client_info', 'client_info', client_info, methods=['GET', 'POST'])
app.add_url_rule('/navigator_info', 'navigator_info', navigator_info, methods=['GET', 'POST'])
app.add_url_rule('/', 'index', index, methods=['POST', 'GET'])
#app.add_url_rule('/results', 'results', results, methods=['POST', 'GET'])
app.add_url_rule('/profile', 'profile', profile, methods=['GET', 'POST'])
app.add_url_rule('/results_navigator', 'results_navigator', results_navigator, methods=['POST', 'GET'])
app.add_url_rule('/results_provider', 'results_provider', results_provider, methods=['POST', 'GET'])
app.add_url_rule('/profile_provider/<int:provider_id>', 'profile_provider', profile_provider, methods=['POST', 'GET'])
app.add_url_rule('/profile_navigator', 'profile_navigator', profile_navigator, methods=['POST', 'GET'])
app.add_url_rule('/review/<int:provider_id>', 'review', review, methods=['POST', 'GET'])
