from django.urls import path

from blog import views

urlpatterns = [
    path("home/", views.blog_home),
    path("post-view/<int:post_id>/", views.blog_post_view),
    path("post-write/", views.blog_post_write)
]
