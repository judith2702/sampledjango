import os
import django
import random
from faker import Faker
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
django.setup()

from first_app.models import AccessRecord, Webpage, Topic, Persons

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))
    
    return t

def populate(N=5):
    for _ in range(N):
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date_object()
        fake_name = fakegen.company()
        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_email = fakegen.email()

        webpg, _ = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)

        user, _ = Persons.objects.get_or_create(
            first_name=fake_fname,
            last_name=fake_lname,
            email=fake_email
        )

        AccessRecord.objects.get_or_create(name=webpg, date=fake_date)

if __name__ == '__main__':
    print("Populating script running...")
    populate(20)
    print("Populating complete.")
