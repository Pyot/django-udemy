from django import forms
from django.core import validators
from login.models import User


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
