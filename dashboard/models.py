from django.db import models


# Create your models here.

class UserManager(models.Manager):

  def register_new_user(self, username, first_name, last_name, interested_orgs, major, year, hobbies, favorites, curr_skills,
                       look_to_learn, self_descriptor, where_from, residence_area):
    user = self.create(username=username, first_name=first_name, last_name=last_name, interested_orgs=interested_orgs, major=major,
                       year=year,
                       hobbies=hobbies, favorites=favorites, curr_skills=curr_skills, look_to_learn=look_to_learn,
                       self_descriptor=self_descriptor, where_from=where_from, residence_area=residence_area)
    return user

class User(models.Model):
  username = models.CharField(max_length=250, primary_key=True)
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  interested_orgs = models.CharField(max_length=200)
  major = models.CharField(max_length=100)
  year = models.CharField(max_length=100)
  hobbies = models.CharField(max_length=200)
  favorites = models.CharField(max_length=500)
  curr_skills = models.CharField(max_length=500)
  look_to_learn = models.CharField(max_length=500)
  self_descriptor = models.CharField(max_length=150)
  where_from = models.CharField(max_length=150)
  residence_area = models.CharField(max_length=100)

  users = UserManager()
