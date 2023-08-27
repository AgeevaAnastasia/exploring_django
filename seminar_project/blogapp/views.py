from django.shortcuts import render
from .models import Author, Post


def get_posts(request, author_id):
    posts = Post.objects.filter(author__pk=author_id)
    context = {'posts': posts}
    return render(request, 'blogapp/posts.html', context)


def get_post(request, post_id):
    post = Post.objects.filter(pk=post_id).first
    # post.views += 1
    # post.save()
    context = {'post': post}
    return render(request, 'blogapp/post.html', context)