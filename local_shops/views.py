from django.shortcuts import render

from shopping.models import Shop
from blog.models import Blog


def local_shops(request):
    shop_list = Shop.objects.all().order_by("-pk")
    context = {
        "shop_list": shop_list
    }
    return render(request, "local_shops/local-home.html", context)
