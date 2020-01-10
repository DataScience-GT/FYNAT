from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField() #you can pass the parameter required = false to make this field optional but by default it is set to be true

    class Meta:
        model = User #whenever form validates a new user is created
        fields = ['username', 'email', 'password1', 'password2']
