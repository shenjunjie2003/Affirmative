"""
views.py
This file is the implementation of the routes for the application.
"""

import random
from flask import render_template, request, redirect, url_for, flash, session, jsonify
from affirmative_app import app
from affirmative_app import db
from sqlalchemy import text
from affirmative_app.models import *
from affirmative_app.globals import *
from affirmative_app.helpers import *
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Generate demo data and retrieve the care navigator ID
        navigator_id = generate_demo_data()
        
        # Flash a message saying demo data has been generated
        flash('Demo data has been generated successfully. You are now logged in as the demo navigator.')

        # Set the unique navigator ID in the session
        session['user_id'] = navigator_id
        
        # Redirect to the index page
        return redirect(url_for('index'))

    # If it's a GET request, render the login page
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
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # Create new User instance
        new_user = User(
            user_name=username,
            password=hashed_password,
            role=role
        )

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

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
                city=city,
                state=state,
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
    
    if 'user_id' not in session:  
        return redirect(url_for('login'))
    
    care_navigator_id = session['user_id']

    surgical_procedures = [
        'Orchiectomy', 'Vaginoplasty', 'Hysterectomy', 'Oophrectomy',
        'Metidoplasty', 'Phalloplasty', 'Breast Augmentation', 'Breast Removal',
        'Facial Reconstructive', 'Body Contouring', 'Electrolysis',
        'Hair removal - laser', 'Hair Transplantation'
    ]
    psychological_procedures = [
        'Counseling with a social worker', 'Psychologist', 'Other Practitioner', 'Psychiatric Care', 'Medical Letter'
    ]

    patients = db.session.query(Patient).join(
        CareNavigatorPatientRelate,
        CareNavigatorPatientRelate.patient_id == Patient.user_ID
    ).filter(
        CareNavigatorPatientRelate.care_navigator_id == care_navigator_id
    ).limit(4).all()

    def get_gender_string(gender_number):
        try:
            gender_number = int(gender_number)
        except ValueError:
            return "Unknown"
        return gender_table_reverse.get(gender_number, "Unknown")
    
    
    for patient in patients:
        patient.display_gender = get_gender_string(patient.preferred_gender)
        saved_providers = db.session.query(Provider.name).join(
            PatientProviderSaved,
            PatientProviderSaved.provider_id == Provider.provider_ID
        ).filter(
            PatientProviderSaved.patient_id == patient.user_ID
        ).all()
        patient.saved_provider_names = [provider.name for provider in saved_providers]

    return render_template('index.html', patients=patients,
                           surgical_procedures=surgical_procedures,
                           psychological_procedures=psychological_procedures)


def results(procedure):

    if request.method == 'POST':
        service = procedure.lower()
        print(f"Received procedure: {service}")
        search_results = (
            Provider.query
            .join(ProviderService, Provider.provider_ID == ProviderService.provider_id)
            .join(Service, ProviderService.service_id == Service.service_ID)
            .filter(Service.name == service)
            .limit(5)
            .all()
        )
        return render_template('results.html', results=search_results, procedure=procedure, count = len(search_results))
    
    return render_template('results.html', procedure=procedure)


def apply_filters():
    # Extract query parameters
    distance = request.args.get('distance', default=None, type=int)
    procedure = request.args.get('procedure', default=None)
    gender = gender_table.get(request.args.get('gender', ''), None)
    meeting_form = availability_table.get(request.args.get('meetingForm', ''), None)
    language = language_dict.get(request.args.get('language', ''), None)
    insurance = insurance_dict.get(request.args.get('insurance', ''), None)

    # Initial query to get providers in the given category
    query = (
        Provider.query
        .join(ProviderService, Provider.provider_ID == ProviderService.provider_id)
        .join(Service, ProviderService.service_id == Service.service_ID)
        .filter(Service.name == procedure)
    )

    # Apply additional filters with explicit joins
    if gender is not None:
        query = query.filter(Provider.gender == gender)
    if meeting_form is not None:
        query = query.filter(Provider.availability == meeting_form)

    # For language and insurance, ensure explicit joins with the many-to-many relationship tables
    if language is not None:
        query = query.join(ProviderLanguage, Provider.provider_ID == ProviderLanguage.provider_id).filter(ProviderLanguage.language_id == language)
    if insurance is not None:
        query = query.join(ProviderInsurance, Provider.provider_ID == ProviderInsurance.provider_id).filter(ProviderInsurance.insurance_id == insurance)


    # Execute the query
    filtered_results = query.all()
    base_zip_code = distance if distance is not None else 48105
    filtered_results.sort(key=lambda provider: abs(int(provider.zip_code or 0) - base_zip_code))


    # If fewer than 4 results, give random results
    if len(filtered_results) < 4:
        # random.sample may raise a ValueError if the sample size is larger than the population size
        # Therefore, ensure the sample size is not larger than the length of filtered_results
        sample_size = min(5, len(filtered_results))
        results = random.sample(filtered_results, sample_size)
        for provider in results:
            provider.label = "Not Match but Recommended"
    else:
        # Assign labels to the first four results
        results = filtered_results[:4]  # Get the first four results
        results[0].label = "Best Match"  # Assign "Best Match" to the first result
        
        # Choose three unique random labels for the next three results
        remaining_labels = [label for key, label in label_dict.items() if key != 0]
        random_labels = random.sample(remaining_labels, 3)
        
        for i in range(1, 4):  # Assign labels to the second, third, and fourth results
            results[i].label = random_labels[i - 1]

    # Convert the results to a list of dictionaries (or a similar structure that can be JSON serialized)
    filtered_results_dicts = [provider_to_dict(provider) for provider in results]

    return jsonify(filtered_results_dicts)

def provider_to_dict(provider):
    # Convert a Provider object to a dictionary
    provider_dict = {
        'provider_ID': provider.provider_ID,
        'name': provider.name,
        'pronoun': provider.pronoun,
        'location': provider.location,
        'specialties': provider.specialties,
        'languages': provider.languages,
    }
    if hasattr(provider, 'label'):
        provider_dict['label'] = provider.label
    return provider_dict
        
@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    user = User.query.get(user_id)

    if user.role == 0:  # Client
        client = Client.query.get(user_id)
        return render_template('client_profile.html', client=client, user=user)
    elif user.role == 1:  # Care Navigator
        navigator = CareNavigator.query.get(user_id)
        return render_template('navigator_profile.html', navigator=navigator, user=user)
    else:
        flash('Invalid user role.')
        return redirect(url_for('login'))
    
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

    
@app.route('/edit-profile', methods=['GET', 'POST'])
def edit_profile():
    if 'user_id' not in session:
        return redirect(url_for('index'))

    user_id = session['user_id']
    user = User.query.get(user_id)

    if request.method == 'POST':
        # Check if it's a client or navigator
        if user.role == 0:  # Client
            client = Client.query.get(user_id)
            client.name = request.form['name']
            client.pronoun = request.form['pronoun']
            client.city = request.form['city']
            client.state = request.form['state']
            # Process the uploaded file if it exists
            if 'profile_picture' in request.files:
                file = request.files['profile_picture']
                if file and file.filename and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    user.profile_picture = os.path.join('uploads', filename)
            db.session.commit()
            flash('Client profile updated successfully!')
            return redirect(url_for('profile'))

        elif user.role == 1:  # Care Navigator
            navigator = CareNavigator.query.get(user_id)
            navigator.name = request.form['name']
            navigator.pronoun = request.form['pronoun']
            navigator.email = request.form['email']
            navigator.insurance = request.form['insurance']
            navigator.zip_code = request.form['zip_code']
            navigator.state = request.form['state']
            navigator.city = request.form['city']
            navigator.self_description = request.form['self_description']
            navigator.trans_caregiving_experience = request.form['trans_caregiving_experience']
            navigator.additional_experience = request.form['additional_experience']
            
            # Process the uploaded file if it exists
            if 'profile_picture' in request.files:
                file = request.files['profile_picture']
                if file and file.filename and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    user.profile_picture = os.path.join('uploads', filename)

            db.session.commit()
            flash('Care Navigator profile updated successfully!')
            return redirect(url_for('profile'))

        # After updating, redirect back to the profile page
        return redirect(url_for('profile'))

    # Render the appropriate edit form based on the user role
    if user.role == 0:  # Client
        client = Client.query.get(user_id)
        return render_template('edit_client_profile.html', client=client, user=user)
    elif user.role == 1:  # Care Navigator
        navigator = CareNavigator.query.get(user_id)
        return render_template('edit_navigator_profile.html', navigator=navigator, user=user)
    else:
        flash('Invalid user role.')
        return redirect(url_for('index'))

       
def profile_navigator():
    return render_template('profile_navigator.html')

def profile_provider(provider_id):
    provider = Provider.query.filter_by(provider_ID=provider_id).first()
    return render_template('profile_provider.html', provider=provider)


def review(provider_id):
    # Retrieve data for the specific doctor based on the doctor_id
    provider = Provider.query.filter_by(provider_ID=provider_id).first()
    return render_template('review.html', doctor=provider, questions=questions)

questions = [
    "I am satisfied with my overall experience with this doctor.",
    "The doctor seems knowledgeable about the latest practice.",
    "The doctor seems knowledgeable about the trans community.",
    "The doctor listened attentively to my concerns and questions during my appointment.",
    "The doctor explained my condition and treatment options clearly and in a way I could understand.",
    "The doctor's recommendations and treatment were effective in addressing my health concerns.",
    "I felt comfortable discussing my medical history and concerns with the doctor.",
    "The doctor's bedside manner and interpersonal skills were satisfactory.",
    "I would recommend this doctor to other people.",
    "Did the doctor or the doctor office help you with the insurance process?"
]

@app.route('/get_result_details/<int:provider_id>')
def get_result_details(provider_id):
    # Find the provider by ID
    provider = Provider.query.filter_by(provider_ID=provider_id).first()    

    if provider:
        # Convert the provider object to a dictionary
        provider_data = {
            "id": provider.provider_ID,
            "name": provider.name,
            "pronoun": provider.pronoun,
            "location": provider.location,
            "email": provider.email,
            "insurance": provider.insurance,
            "website": provider.website,
            "zip_code": provider.zip_code,
            "finances": provider.finances,
            "qualifications": provider.qualifications,
            "profile_picture": provider.profile_picture,
            "phone_number": provider.phone_number,
            "gender": provider.gender,
            "availability": provider.availability,
            "category": provider.category,
            "education": provider.education,
            "hospital": provider.hospital,
            "languages": provider.languages
            # Add more fields as needed
        }
        return jsonify(provider_data)
    else:
        return jsonify({"error": "Provider not found"})
           
@app.route('/update_bookmarks', methods=['POST'])
def update_bookmarks():
    data = request.json
    provider_id = data['provider_id']
    checked_patients = set(map(int, data['checked_patients']))
    unchecked_patients = set(map(int, data['unchecked_patients']))
    
    # Handle checked patients
    for patient_id in checked_patients:
        # Check if the entry already exists to avoid duplicates
        exists = PatientProviderSaved.query.filter_by(patient_id=patient_id, provider_id=provider_id).first()
        if not exists:
            new_bookmark = PatientProviderSaved(patient_id=patient_id, provider_id=provider_id)
            db.session.add(new_bookmark)

    # Handle unchecked patients
    for patient_id in unchecked_patients:
        PatientProviderSaved.query.filter_by(patient_id=patient_id, provider_id=provider_id).delete()

    db.session.commit()
    return jsonify(status='success'), 200
