from django.shortcuts import render
from django.http import HttpResponseRedirect

from blog.models import Post


def blog_home(request):
    post_list = Post.objects.all()
    context = {
        "post_list": post_list
    }
    return render(request, "blog/index.html", context)


def blog_post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        "post": post
    }
    return render(request, "blog/post.html", context)


def blog_post_write(request):
    if request.method == "POST":
        print(request.POST["hidden_"])
        new_post = Post()
        new_post.title = request.POST["title"]
        new_post.content = request.POST["content"]
        new_post.likes = 0
        new_post.save()
        return HttpResponseRedirect("/blog/post-write")

    return render(request, "blog/create.html")
