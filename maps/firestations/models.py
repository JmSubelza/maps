from django.db import models

class Station(models.Model):
    address = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()

