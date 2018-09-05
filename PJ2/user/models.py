from django.db import models

# Create your models here.
class USER(models.Model):
    username = models.TextField(max_length=15)
    password = models.TextField(max_length=8)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username