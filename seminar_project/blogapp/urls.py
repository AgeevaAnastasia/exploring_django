from django.urls import path
from .views import get_posts, get_post

urlpatterns = [
    path('posts/<int:author_id>/', get_posts),
    path('post/<int:post_id>/', get_post, name='post'),
]