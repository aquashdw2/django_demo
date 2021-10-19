from django.shortcuts import render


def payment_cart(request):
    return render(request, "payment/cart.html")


def payment_purchase(request):
    return render(request, "payment/purchase.html")


def payment_complete(request):
    return render(request, "payment/complete.html")
