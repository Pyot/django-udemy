import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

import random
from AppTwo.models import User
from faker import Faker

fakegen =  Faker()

def populate (N=5):
    for entry in range(N):
        #create fake data
        fake_name =  fakegen.name()
        fake_last_name =  fakegen.name()
        fake_email = fakegen.email()


        #create new User
        user = User.objects.get_or_create( first_name = fake_name, last_name = fake_last_name,  email = fake_email)[0]

if __name__ == '__main__':
    print('start populate Users!')
    populate(20)
    print('END')
