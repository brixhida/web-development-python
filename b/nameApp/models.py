from django.db import models

class PetInterest(models.Model):

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    pet_choice = models.CharField(max_length=50)
    more_info = models.CharField(max_length=50)
 

# python manage.py makemigrations
# python manage.py migrate

# python manage.py createsuperuser

# python manage.py runserver