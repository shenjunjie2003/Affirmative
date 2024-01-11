from affirmative_app import db, app
from affirmative_app.models import ProviderService
import random

def populate_provider_service():
    provider_ids = list(range(3, 51))  # Provider IDs from 3 to 50
    service_ids = list(range(1, 20))   # Service IDs from 1 to 19

    for provider_id in provider_ids:
        for service_id in service_ids:
            provider_service_entry = ProviderService(
                provider_id=provider_id,
                service_id=service_id
            )
            db.session.add(provider_service_entry)
    db.session.commit()

with app.app_context():
    populate_provider_service()
