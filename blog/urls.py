from django.urls import path

from blog import views


app_name = "blog"
urlpatterns = [
    path("home/", views.blog_home, name="home"),
    path("post-view/<int:post_id>/", views.blog_post_view, name="post-view"),
    path("post-write/", views.blog_post_write, name="post-write"),
    path("post-edit/<int:post_id>/", views.blog_post_edit, name="post-edit"),
    path("post-delete/<int:post_id>/", views.blog_post_delete, name="post-delete")
]
