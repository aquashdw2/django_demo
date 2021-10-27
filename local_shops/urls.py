from django.urls import path

from local_shops import views


app_name = "local"
urlpatterns = [
    path("local-shops/", views.local_shops, name="home"),
]
