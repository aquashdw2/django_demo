from django.shortcuts import render


def payment_cart(request):
    context = {

    }
    return render(request, "payment/cart.html", context)


def payment_purchase(request):
    context = {

    }
    return render(request, "payment/purchase.html", context)


def payment_complete(request):
    context = {

    }
    return render(request, "payment/complete.html", context)
