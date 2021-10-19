from django.urls import path

from shopping import views


urlpatterns = [
    path("", views.shopping_home),
    path("admin/", views.shopping_admin),
    path("item/", views.shopping_item)
]

