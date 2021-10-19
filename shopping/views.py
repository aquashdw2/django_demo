from django.shortcuts import render


def shopping_home(request):
    return render(request, "shopping/index.html")


def shopping_admin(request):
    return render(request, "shopping/admin.html")


def shopping_item(request):
    return render(request, "shopping/item.html")
