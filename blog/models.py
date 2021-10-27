from django.db import models

from shopping.models import Shop


class Blog(models.Model):
    shop = models.OneToOneField(Shop, on_delete=models.SET_NULL, null=True)
    blog_name = models.CharField(max_length=32)
    blog_banner = models.ImageField(
        upload_to="blog/image/banner/",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.SET_NULL,
        null=True,
        related_name="blog_posts"
    )
    title = models.CharField(max_length=32)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PostImage(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.SET_NULL,
        related_name="post_images",
        null=True
    )
    image = models.ImageField(
        upload_to="blog/image/posts/%Y/%m/%d/",
        blank=True,
        null=True,
    )
