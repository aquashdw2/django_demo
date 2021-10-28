from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from accounts.models import Info
from local_shops.models import Area
from shopping.models import Shop
from blog.models import Blog


def sign_up(request):
    context = {

    }
    if request.method == "POST":
        if (
            request.POST.get("username") and
            request.POST.get("password") and
            request.POST.get("password") == request.POST.get("password_check")
        ):
            new_user = User.objects.create_user(
                username=request.POST.get("username"),
                password=request.POST.get("password"),
            )

            new_user_info = Info()
            new_user_info.user = new_user
            if request.POST.get("is_owner"):
                new_user_info.is_shop_owner = True
            else:
                new_user_info.is_shop_owner = False

            area = Area.objects.get(id=1)
            new_user_info.area = area
            new_user_info.save()
            if request.POST.get("is_owner"):
                new_shop = Shop()
                new_shop.user = new_user_info
                new_shop.area = new_user_info.area
                new_shop.latitude = area.latitude
                new_shop.longitude = area.longitude
                new_shop.save()

                new_blog = Blog()
                new_blog.blog_name = f"{new_user.username}의 블로그"
                new_blog.shop = new_shop
                new_blog.save()

            auth.login(request, new_user)

            return redirect("landing:home")
        else:
            context["error"] = "잘못된 입력입니다."

    return render(request, "accounts/sign-up.html", context)


def login(request):
    return render(request, "accounts/login.html")


def logout(request):
    if request.method == "POST":
        auth.logout(request)

    return redirect("landing:home")


def my_page(request):
    return render(request, "accounts/my-page.html")
