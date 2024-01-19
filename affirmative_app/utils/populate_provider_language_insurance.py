from affirmative_app import db, app
from affirmative_app.models import ProviderLanguage, ProviderInsurance
import random

def populate_provider_language():
    unique_entries = set()
    # Ensure each provider_id has at least one entry
    for provider_id in range(1, 101):
        language_id = random.randint(0, 6)
        unique_entries.add((provider_id, language_id))
    # Populate additional random entries until we have 250
    while len(unique_entries) < 250:
        provider_id = random.randint(1, 100)
        language_id = random.randint(0, 6)
        unique_entries.add((provider_id, language_id))

    for provider_id, language_id in unique_entries:
        provider_language_entry = ProviderLanguage(
            provider_id=provider_id,
            language_id=language_id
        )
        db.session.add(provider_language_entry)
    db.session.commit()

def populate_provider_insurance():
    unique_entries = set()
    # Ensure each provider_id has at least one entry
    for provider_id in range(1, 101):
        insurance_id = random.randint(1, 8)
        unique_entries.add((provider_id, insurance_id))
    # Populate additional random entries until we have 400
    while len(unique_entries) < 400:
        provider_id = random.randint(1, 100)
        insurance_id = random.randint(1, 8)
        unique_entries.add((provider_id, insurance_id))

    for provider_id, insurance_id in unique_entries:
        provider_insurance_entry = ProviderInsurance(
            provider_id=provider_id,
            insurance_id=insurance_id
        )
        db.session.add(provider_insurance_entry)
    db.session.commit()

with app.app_context():
    populate_provider_language()
    populate_provider_insurance()