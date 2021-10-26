from django.shortcuts import render


def sign_up(request):
    return render(request, "accounts/sign-up.html")


def login(request):
    return render(request, "accounts/login.html")


def logout(request):
    return render(request, "accounts/log-out.html")


def my_page(request):
    return render(request, "accounts/my-page.html")
