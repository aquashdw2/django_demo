from django.shortcuts import render


def local_shops(request):
    return render(request, "local_shops/local-home.html")
