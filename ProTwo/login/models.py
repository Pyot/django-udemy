from django.db import models

class User(models.Model):
    first_name =  models.CharField(max_length= 120, unique = True)
    last_name = models.CharField(max_length = 120, unique = True)
    email = models.EmailField(unique = True)

    def __str__(self):
        return self.first_name
