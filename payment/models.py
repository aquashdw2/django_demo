from django.db import models

from accounts.models import Info
from shopping.models import Item


class Purchases(models.Model):
    user = models.ForeignKey(
        Info,
        on_delete=models.SET_NULL,
        null=True
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.SET_NULL,
        null=True
    )
    count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=32, null=True)
