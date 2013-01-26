from django.db import models

class Library(models.Model):
    location = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100)
    hours = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=250, null=True, blank=True)
    lat = models.FloatField()
    lng = models.FloatField()

