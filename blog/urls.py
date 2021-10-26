from django.urls import path

from blog import views


app_name = "blog"
urlpatterns = [
    path("<int:blog_id>/", views.shop_blog_home, name="home"),
    path("<int:blog_id>/post/<int:post_id>/", views.shop_blog_post, name="post"),
    path("<int:blog_id>/post/write/", views.shop_blog_post_write, name="write"),
    path("<int:blog_id>/post/<int:post_id>/edit/", views.shop_blog_post_edit, name="edit"),
    path("<int:blog_id>/post/<int:post_id>/delete/", views.shop_blog_post_delete, name="delete")
]
