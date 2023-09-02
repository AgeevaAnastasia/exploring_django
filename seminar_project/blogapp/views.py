from django.shortcuts import render

from . import forms, models
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


def author_form(request):
    message = ''
    if request.method == 'POST':
        form = forms.AuthorForm(request.POST)
        if form.is_valid():
            author = models.Author(name=form.cleaned_data['name'],
                                   lastname=form.cleaned_data['lastname'],
                                   email=form.cleaned_data['email'],
                                   bio=form.cleaned_data['bio'],
                                   birthdate=form.cleaned_data['birthdate'])
            author.save()
            message = 'Автор успешно сохранен'
    else:
        form = forms.AuthorForm()

    return render(request, 'blogapp/base.html',
                  {'form': form, 'message': message, 'title': 'Сохранение автора'})


def post_form(request):
    message = ''
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = models.Post(title=form.cleaned_data['title'],
                               content=form.cleaned_data['content'],
                               public_date=form.cleaned_data['public_date'],
                               category=form.cleaned_data['category'],
                               author=form.cleaned_data['author'],
                               ispublic=form.cleaned_data['ispublic'])
            post.save()
            message = 'Пост успешно сохранен'
    else:
        form = forms.PostForm()

    return render(request, 'blogapp/base.html',
                  {'form': form, 'message': message, 'title': 'Сохранение поста'})
