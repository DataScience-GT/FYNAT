from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model): #Inherit from models.Model
    user = models.OneToOneField(User, on_delete = models.CASCADE) #create one-to-one user profile assignment, also delete users data if their account is removed
    image = models.ImageField(default='default.jpg',upload_to = 'profile_pics') #users can upload a jpg to the profile pics directory

    def __str__(self): # method prints out the profile info in a a readable format
        return f'{self.user.username} Profile'


