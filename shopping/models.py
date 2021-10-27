from django.db import models

from local_shops.models import Area


class Shop(models.Model):
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
