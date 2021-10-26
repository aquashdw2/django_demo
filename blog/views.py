from django.shortcuts import render


def shop_blog_home(request, blog_id):
    return render(request, "blog/blog-home.html")


def shop_blog_post(request, blog_id, post_id):
    return render(request, "blog/blog-post.html")


def shop_blog_post_write(request, blog_id):
    return render(request, "blog/blog-post-write.html")


def shop_blog_post_edit(request, blog_id, post_id):
    return render(request, "blog/blog-post-edit.html")


def shop_blog_post_delete(request, blog_id, post_id):
    return render(request, "blog/blog-post-delete.html")
