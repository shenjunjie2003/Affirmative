"""
Models for affirmative_app.
"""
from . import db

class User(db.Model):
    """User table."""
    __tablename__ = 'user'
    user_ID = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(256), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    role = db.Column(db.Integer, nullable=False)  # 0 for patient, 1 for navigator
    profile_picture = db.Column(db.String(512), nullable=True)  # Path to profile picture

class Client(db.Model):
    __tablename__ = 'client'
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_ID'), primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    pronoun = db.Column(db.String(256), nullable=False)
    city = db.Column(db.String(256), nullable=False)
    state = db.Column(db.String(256), nullable=False)

class CareNavigator(db.Model):
    __tablename__ = 'care_navigator'
    navigator_ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    pronoun = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=True)  
    insurance = db.Column(db.String(256), nullable=True)  
    zip_code = db.Column(db.String(256), nullable=True) 
    state = db.Column(db.String(256), nullable=False)  
    city = db.Column(db.String(256), nullable=False)  
    self_description = db.Column(db.Text, nullable=True)  
    trans_caregiving_experience = db.Column(db.Text, nullable=True) 
    additional_experience = db.Column(db.Text, nullable=True)  

class NavigatorInsurance(db.Model):
    __tablename__ = 'navigator_insurance'
    navigator_id = db.Column(db.Integer, primary_key=True)
    insurance_id = db.Column(db.Integer, primary_key=True)

class Provider(db.Model):
    __tablename__ = 'provider'
    provider_ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    pronoun = db.Column(db.String(256), nullable=False)
    location = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    insurance = db.Column(db.String(256), nullable=False)
    website = db.Column(db.String(256), nullable=False)
    zip_code = db.Column(db.String(256), nullable=False) # Zip code
    finances = db.Column(db.String(256), nullable=False)
    qualifications = db.Column(db.String(256), nullable=False)
    profile_picture = db.Column(db.LargeBinary, nullable=True)  

class ProviderInsurance(db.Model):
    __tablename__ = 'provider_insurance'
    provider_id = db.Column(db.Integer, primary_key=True)
    insurance_id = db.Column(db.Integer, primary_key=True)

class ProviderService(db.Model):
    __tablename__ = 'provider_service'
    provider_id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, primary_key=True)

class Patient(db.Model):
    __tablename__ = 'patient'
    user_ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=False)

class ReviewForProvider(db.Model):
    __tablename__ = 'review_for_provider'
    review_id = db.Column(db.Integer, primary_key=True)
    provider_id = db.Column(db.Integer, primary_key=True)
    review_value = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(1024), nullable=False)

class ReviewForNavigator(db.Model):
    __tablename__ = 'review_for_navigator'
    review_id = db.Column(db.Integer, primary_key=True)
    navigator_id = db.Column(db.Integer, primary_key=True)
    review_value = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(256), nullable=False)

class Service(db.Model):
    __tablename__ = 'service'
    service_ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    broad_service = db.Column(db.Integer, nullable=False) #0 for mental health, 1 for endodermal, 2 for surgery

class Insurance(db.Model):
    __tablename__ = 'insurance'
    insurance_ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)

class SavedNavigator(db.Model):
    __tablename__ = 'saved_navigator'
    client_id = db.Column(db.Integer, primary_key=True)
    navigator_id = db.Column(db.Integer, primary_key=True)

class SavedProvider(db.Model):
    __tablename__ = 'saved_provider'
    client_id = db.Column(db.Integer, primary_key=True)
    provider_id = db.Column(db.Integer, primary_key=True)