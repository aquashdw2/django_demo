from django.urls import path

from local_shops import views


urlpatterns = [
    path("shops-near-me", views.local_shops),
]
