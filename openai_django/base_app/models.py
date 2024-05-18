from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=256)
    place = models.CharField(max_length=256)
    type = models.CharField(max_length=256)