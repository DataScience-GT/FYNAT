from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Post(models.Model):
    class1 = models.CharField(max_length = 500)
    class2 = models.CharField(max_length = 500)
    class3 = models.CharField(max_length = 500)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    date = models.DateTimeField(auto_now=True)