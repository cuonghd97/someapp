from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    fullname = models.TextField(max_length=None)
    address = models.TextField(max_length=None)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    typeuser = models.IntegerField()