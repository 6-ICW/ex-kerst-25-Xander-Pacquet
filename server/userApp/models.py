from django.db import models

# Create your models here.
class User(models.Model):
    login = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    email = models.EmailField()
    role = models.CharField(max_length=25)
    isSuperuser = models.BooleanField()
