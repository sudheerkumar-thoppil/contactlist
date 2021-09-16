from django.db import models

# Create your models here.
class Phonebook(models.Model):
    name = models.CharField(max_length=50)
    phone_num = models.IntegerField()
