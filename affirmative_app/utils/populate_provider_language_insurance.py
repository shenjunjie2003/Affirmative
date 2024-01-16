from affirmative_app import db, app
from affirmative_app.models import ProviderLanguage, ProviderInsurance
import random

def populate_provider_language():
    entries = set()
    while len(entries) < 80:
        provider_id = random.randint(3, 52)
        language_id = random.randint(0, 6)
        entries.add((provider_id, language_id))

    for provider_id, language_id in entries:
        provider_language_entry = ProviderLanguage(
            provider_id=provider_id,
            language_id=language_id
        )
        db.session.add(provider_language_entry)
    db.session.commit()

def populate_provider_insurance():
    entries = set()
    while len(entries) < 80:
        provider_id = random.randint(3, 52)
        insurance_id = random.randint(1, 3)
        entries.add((provider_id, insurance_id))

    for provider_id, insurance_id in entries:
        provider_insurance_entry = ProviderInsurance(
            provider_id=provider_id,
            insurance_id=insurance_id
        )
        db.session.add(provider_insurance_entry)
    db.session.commit()

with app.app_context():
    populate_provider_language()
    populate_provider_insurance()
