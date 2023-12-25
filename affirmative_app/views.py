"""
views.py
This file is the implementation of the routes for the application.
"""

from flask import render_template, request, redirect, url_for, flash, session
from affirmative_app import app
from affirmative_app import db
from sqlalchemy import text
from affirmative_app.models import *
from werkzeug.security import generate_password_hash


def login():
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Extract the form data
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        name = request.form['name']
        pronoun = request.form['pronoun']
        city = request.form['city']
        state = request.form['state']

        # Check if the username already exists
        user = User.query.filter_by(user_name=username).first()
        if user:
            flash('Username already exists.')
            return redirect(url_for('register'))

        # Hash the password for security
        hashed_password = generate_password_hash(password, method='sha256')

        # Create new User instance
        new_user = User(
            user_name=username,
            password=hashed_password,
            role=role
        )

        # Add the new user to the database
        db.session.add(new_user)
        # Create either Client or CareNavigator instance
        if role == '0':  # Client
            new_client = Client(
                user_id=new_user.user_ID,
                name=name,
                pronoun=pronoun,
                city=city,
                state=state
            )
            db.session.add(new_client)
        elif role == '1':  # Care Navigator
            new_navigator = CareNavigator(
                navigator_ID=new_user.user_ID,
                name=name,
                pronoun=pronoun,
                location=f"{city}, {state}"
            )
            db.session.add(new_navigator)

        db.session.commit()

        # Redirect to the index page after successful registration
        return redirect(url_for('index'))
    
    return render_template('register.html')

# Additional information pages
@app.route('/client_info', methods=['GET', 'POST'])
def client_info():
    if request.method == 'POST':
        # Process and save client information
        pass
    return render_template('client_info.html')

@app.route('/navigator_info', methods=['GET', 'POST'])
def navigator_info():
    if request.method == 'POST':
        # Process and save navigator information
        pass
    return render_template('navigator_info.html')

#test database connection
def test_db_connection():
    try:
        result = db.session.execute(text('SELECT 1'))
        print('Database connection successful!')
        return 'Database connection successful!'
    except Exception as e:
        print(f'Database connection error: {str(e)}')
        return f'Database connection error: {str(e)}'

def index():
    return render_template('index.html')


# Results page
def results():
    if request.method == 'POST':
        # Get user input from the form
        category = request.form.get('category')
        zip = request.form.get('location')

        if category == 'care navigator':
            care_navigator_results = CareNavigator.query.filter(CareNavigator.zip_code.ilike(f'%{zip}%')).all()
            return render_template('results.html', results=care_navigator_results)
        else:
            search_results = (
                Provider.query
                .join(ProviderService, Provider.provider_ID == ProviderService.provider_id)
                .join(Service, ProviderService.service_id == Service.service_ID)
                .filter(Service.broad_service == category, Provider.zip_code == zip)
                .all()
           )
            return render_template('results.html', results=search_results)