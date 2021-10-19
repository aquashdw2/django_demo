from django.shortcuts import render


def blog_home(request):
    return render(request, "blog/index.html")


def blog_post_view(request):
    return render(request, "blog/post.html")


def blog_post_write(request):
    return render(request, "blog/create.html")
