from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    post = Post.published.all()
    return render(request, "blog/post/detail.html", {"post": post})


def post_detail(request, id: int):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, "blog/post/detail.html", {"post": post})


# Create your views here.
