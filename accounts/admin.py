from django.contrib import admin
from .models import Profile #sync the Profile class from models.py

# Register your models here.

admin.site.register(Profile) 
