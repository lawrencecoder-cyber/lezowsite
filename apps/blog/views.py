from django.shortcuts import render, redirect
from .selectors import BlogSelector
from .services import BlogService
from .models import Post


def blog_list_view(request):
    posts = BlogSelector.published_posts()

    return render(request, "blog/list.html", {
        "posts": posts
    })


def blog_detail_view(request, slug):
    post = BlogSelector.get_post_by_slug(slug)

    return render(request, "blog/detail.html", {
        "post": post
    })


def create_post_view(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        tags = request.POST.get("tags")

        BlogService.create_post(request.user, title, content, tags)

        return redirect("blog_list")

    return render(request, "blog/create.html")
