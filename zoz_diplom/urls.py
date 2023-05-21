from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('posts/', include('post.urls')),
    path('shop/', include('shop.urls')),
    path('about/', include('about.urls')),
    path('profile/', include('profiles.urls')),
]
