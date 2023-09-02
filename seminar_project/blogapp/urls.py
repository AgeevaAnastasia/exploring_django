from django.urls import path
from .views import get_posts, get_post, author_form, post_form

urlpatterns = [
    path('posts/<int:author_id>/', get_posts),
    path('post/<int:post_id>/', get_post, name='post'),
    path('author/', author_form, name='author'),
    path('create_post/', post_form, name='create_post'),
]