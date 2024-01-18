"""Helper functions for the affirmative app."""

from affirmative_app import db, app
from affirmative_app.models import *

def generate_patients_with_relations(db_session, care_navigator_id):
    # Define the data for each patient
    patients_data = [
        {'name': 'Lake Green', 'email': 'lakegreen@gmail.com', 'state': 'MI', 'city': 'Ann Arbor',
         'address': '123123 Max Rd', 'environment': '0', 'insurance': 'Blue Cross',
         'accessibility': 'Hearing Accessibility', 'ethnicity': 'Asian', 'gender': 'Male',
         'language': 'English', 'preferred_gender': '1', 'preferred_ethnicity': 'Asian'},
        
        {'name': 'Emily Link', 'email': 'emilylink@123mail.com', 'state': 'MI', 'city': 'Ann Arbor',
         'address': '123123 St', 'environment': '2', 'insurance': 'Humana',
         'accessibility': 'None', 'ethnicity': 'White', 'gender': 'Female',
         'language': 'English', 'preferred_gender': '0', 'preferred_ethnicity': 'White'},
        
        {'name': 'Luke Lance', 'email': 'lukelance@gmail.com', 'state': 'MI', 'city': 'Detroit',
         'address': '123123 Main St', 'environment': '3', 'insurance': 'McLaren',
         'accessibility': 'Hearing Accessibility', 'ethnicity': 'Black', 'gender': 'Male',
         'language': 'English', 'preferred_gender': '1', 'preferred_ethnicity': 'Black'},
        
        {'name': 'Julia Nancy', 'email': 'julianancy@gmail.com', 'state': 'MI', 'city': 'Troy',
         'address': '1324 South St', 'environment': '1', 'insurance': 'Aetna',
         'accessibility': 'Hearing accessibility', 'ethnicity': 'Asian', 'gender': 'Female',
         'language': 'English', 'preferred_gender': '0', 'preferred_ethnicity': 'Asian'}
    ]

    # Create and add each patient to the session
    for patient_data in patients_data:
        patient = Patient(**patient_data)
        db_session.add(patient)
        db_session.flush()  # This will assign an ID to each patient without committing the transaction

        # Create a CareNavigatorPatientRelate instance for each patient
        care_nav_patient_rel = CareNavigatorPatientRelate(
            care_navigator_id=care_navigator_id,
            patient_id=patient.user_ID
        )
        db_session.add(care_nav_patient_rel)

    # Commit the session to save everything to the database
    db_session.commit()

# Function to generate a care navigator and four patients
def generate_demo_data():
    # Create a dummy care navigator
    care_navigator = CareNavigator(
        name="Demo Navigator",
        pronoun="They/Them",
        email="demo@navigator.com",
        state="Demo State",
        city="Demo City"
    )
    db.session.add(care_navigator)
    db.session.flush()  # This will assign an ID to the navigator without committing

    # Generate four patients and associate them with the dummy navigator
    generate_patients_with_relations(db.session, care_navigator.navigator_ID)

    # Commit the session to save the care navigator and patients
    db.session.commit()

    # Return the ID of the newly created care navigator
    return care_navigator.navigator_ID