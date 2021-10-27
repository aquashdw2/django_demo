from django.db import models
from django.contrib.auth.models import User

from local_shops.models import Area


class Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)
    is_shop_owner = models.BooleanField(default=False)
