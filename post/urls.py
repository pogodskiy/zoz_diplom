from django.urls import path
from .views import *

urlpatterns = [
    path('create_post/', create_post, name='create_post'),
    # path('', posts, name='posts'),
    path('post_update/', post_update, name='post_update'),
    path('post_delete/', post_delete, name='post_delete'),
    path('posts_user/', posts_user, name='posts_user'),
    path('posts_detail/<post_id>', posts_detail, name='post_detail'),
    path('posts/', posts, name='posts'),
    path('posts/<int:cat_selected>/', posts, name='posts'),

]