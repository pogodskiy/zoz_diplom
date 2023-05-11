
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
    path('deleter/', user_delete, name='deleter'),
    path('profile/', profile, name='profile'),
]