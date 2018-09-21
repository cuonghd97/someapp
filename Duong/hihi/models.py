from django.db import models

# Create your models here.

class userInfo(models.Model):
    userName = models.TextField(max_length=None)
    email = models.TextField(max_length=None)
    birthday = models.TextField(max_length=None)
class Code(models.Model):
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.code