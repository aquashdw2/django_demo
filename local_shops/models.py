from django.db import models


class Area(models.Model):
    area_code = models.IntegerField()
    city_name = models.CharField(max_length=32)
    county_name = models.CharField(max_length=32)
    town_name = models.CharField(max_length=32)
    latitude = models.FloatField()
    longitude = models.FloatField()
