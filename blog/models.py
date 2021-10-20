from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField()
    likes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"title: {self.title}"
