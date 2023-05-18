from django.urls import path
from .views import *

urlpatterns = [
    path('create_post/', create_post, name='create_post'),
    # path('', posts, name='posts'),
    path('posts_detail/<post_id>', posts_detail, name='post_detail'),
    path('posts/', posts, name='posts'),
    path('posts/<int:cat_selected>/', posts, name='posts'),

]