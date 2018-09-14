from django.db import models

# Create your models here.
class table(models.Model):
    names = models.TextField()
    age = models.CharField(max_length = 5)

    # def __str__(self):
    #     return self.names