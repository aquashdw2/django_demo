from django.urls import path

from shopping import views


app_name = "shop"
urlpatterns = [
    path("", views.shopping_home, name="home"),
    path("admin/", views.shopping_admin),
    path("item/", views.shopping_item)
]

