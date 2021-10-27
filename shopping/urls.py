from django.urls import path

from shopping import views


app_name = "shop"
urlpatterns = [
    path("<int:shop_id>/", views.shop_home, name="home"),
    path("<int:shop_id>/item/<int:item_id>/", views.shop_item, name="item"),
    path("<int:shop_id>/admin/", views.shop_admin, name="admin"),
    path("<int:shop_id>/admin/item/add/", views.shop_admin_add_item, name="item-add"),
    path("<int:shop_id>/admin/item/<int:item_id>/edit/", views.shop_admin_edit, name="item-edit"),
]
