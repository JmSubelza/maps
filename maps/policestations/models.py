from django.db import models

class Station(models.Model):
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=250)
    lat = models.FloatField()
    lng = models.FloatField()

