from django.urls import path

from payment import views


urlpatterns = [
    path("cart/", views.payment_cart),
    path("purchase/", views.payment_purchase),
    path("complete/", views.payment_complete),
]