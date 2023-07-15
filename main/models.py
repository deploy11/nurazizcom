from django.db import models

# Create your models here.
class Portfolio(models.Model):
    url = models.CharField(max_length=250)
    image = models.ImageField(upload_to='rasmlar/')

class Contact(models.Model):
    name = models.CharField(max_length=250)
    tel = models.CharField(max_length=250)
    msg = models.TextField()