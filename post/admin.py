from django.contrib import admin
from .models import Post, CatPost

admin.site.register(Post)
admin.site.register(CatPost)