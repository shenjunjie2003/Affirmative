from affirmative_app import db, app
from affirmative_app.models import ProviderService
import random

def populate_provider_service():
    entries = set()
    provider_ids = list(range(1, 101))  # Provider IDs from 1 to 100
    service_ids = list(range(1, 20))    # Service IDs from 1 to 19

    # Let's assume you want to create 300 unique provider-service pairs
    while len(entries) < 1000:
        provider_id = random.choice(provider_ids)
        service_id = random.choice(service_ids)
        entry = (provider_id, service_id)

        if entry not in entries:
            entries.add(entry)
            provider_service_entry = ProviderService(
                provider_id=provider_id,
                service_id=service_id
            )
            db.session.add(provider_service_entry)

    db.session.commit()

with app.app_context():
    populate_provider_service()