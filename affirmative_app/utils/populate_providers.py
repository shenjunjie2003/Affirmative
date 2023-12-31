from affirmative_app import db, app
from affirmative_app.models import Provider
from faker import Faker
import random
import os

fake = Faker()

def get_placeholder_profile_pic():
    # Construct an absolute path to the directory where this script is located
    script_dir = os.path.dirname(__file__)
    # Now construct the absolute path to the image file
    image_path = os.path.join(script_dir, '..', 'static', 'uploads', 'default_profile_pic.webp')
    # Use the absolute path to open the file
    with open(image_path, 'rb') as image_file:
        return image_file.read()

def create_fake_provider(placeholder_image_data):
    name = fake.name()
    pronoun = random.choice(['He/Him', 'She/Her', 'They/Them'])
    location = fake.address()
    email = fake.email()
    insurance = random.choice(['Yes', 'No'])
    website = fake.url()
    zip_code = fake.zipcode()
    finances = "Individual Sessions $" + str(random.randint(50, 200))
    qualifications = fake.sentence(nb_words=6)
    phone_number = fake.phone_number()
    if len(phone_number) > 20:
        phone_number = phone_number[:20]
    gender = random.randint(0, 5)
    availability = random.randint(0, 2)
    category = random.randint(0, 17)

    provider = Provider(
        name=name,
        pronoun=pronoun,
        location=location,
        email=email,
        insurance=insurance,
        website=website,
        zip_code=zip_code,
        finances=finances,
        qualifications=qualifications,
        profile_picture=placeholder_image_data,
        phone_number=phone_number,
        gender=gender,
        availability=availability,
        category=category
    )
    return provider

def populate_database(num_entries=10, placeholder_image_data=None):
    for _ in range(num_entries):
        provider = create_fake_provider(placeholder_image_data)
        db.session.add(provider)
    db.session.commit()


with app.app_context():
    # Load placeholder profile picture data
    placeholder_image_data = get_placeholder_profile_pic()
    # Populate the database with 50 entries, using the placeholder profile picture
    populate_database(50, placeholder_image_data)
