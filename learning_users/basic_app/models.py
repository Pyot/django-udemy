from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    #dodajmey dodatkowe informacje do juz stworzonego w django modelu User
    user =  models.OneToOneField(User)

    #dodatkowe pole
    portfolio_site = models.URLField(blank=True)
    #jeżeli pracujemy ze zdjeciami potrzebujmey biblioteki PILLOW pip install pillow
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
