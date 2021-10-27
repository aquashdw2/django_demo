from django.urls import path

from payment import views


app_name = "payment"
urlpatterns = [
    path("cart/", views.payment_cart, name="cart"),
    path("purchase/", views.payment_purchase, name="purchase"),
    path("results/", views.payment_complete, name="results"),
]
