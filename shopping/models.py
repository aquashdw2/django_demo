from django.db import models

from local_shops.models import Area


class Shop(models.Model):
    user = models.OneToOneField(
        'accounts.Info',
        on_delete=models.SET_NULL,
        related_name="owning_shop",
        null=True
    )
    area = models.ForeignKey(
        Area,
        on_delete=models.SET_NULL,
        null=True,
        related_name="area_shops"
    )
    latitude = models.FloatField()
    longitude = models.FloatField()


class Item(models.Model):
    shop = models.ForeignKey(
        Shop,
        on_delete=models.SET_NULL,
        null=True
    )
    name = models.CharField(max_length=128)
    price = models.IntegerField()


class ItemImages(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete=models.SET_NULL,
        related_name="item_images",
        null=True
    )
    image = models.ImageField(
        upload_to="shop/image/item/%Y/%m/%d/",
        blank=True,
        null=True,
    )
