from django.db import models


class ShopItem(models.Model):
    item_name = models.CharField(max_length=128)
    price = models.IntegerField()
    description = models.TextField()
    shop_info = models.CharField(max_length=64)
