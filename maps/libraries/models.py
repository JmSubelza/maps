from django.db import models

class Library(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    address = models.CharField(max_length=100)
