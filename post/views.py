from django.shortcuts import render, redirect, get_object_or_404
from post.models import Post
from django.contrib.auth.decorators import login_required
from post.forms import PostForm
from user.models import User
from django.contrib.auth import get_user
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required


from django.shortcuts import render
from .models import Post, CatPost

def posts(request, cat_selected=0):
    cat = CatPost.objects.all()
    if cat_selected == 0:
        posts = Post.objects.all()
    else:
        category = get_object_or_404(CatPost, pk=cat_selected)
        posts = Post.objects.filter(cat=category)

    context = {'cat': cat, 'cat_selected': cat_selected, 'posts': posts}
    return render(request, 'post/posts.html', context)



@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return render(request, 'user/home.html')
    else:
        form = PostForm()
    return render(request, 'post/create_post.html', {'form': form})




def posts_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        context = {'post': post}
        return render(request, 'post/post_detail.html', context)
    else:
        context = {'post': post}
        return render(request, 'post/post_detail.html', context)




@login_required
def post_update(request, product_id):
    post = get_object_or_404(Post, id=product_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(
                'posts:list')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_update.html', {'form': form, 'post': post})

@login_required
def post_delete(request, product_id):
    post = get_object_or_404(Post, id=product_id)
    if request.method == 'POST':
        post.delete()
        return redirect(
            'posts:list')
    return render(request, 'post_delete.html', {'post': post})


def posts_user(request, name):
    user = User.objects.get(username=name)
    posts = Post.objects.filter(author=user)
    context = {'user': user, 'posts': posts}
    return render(request, 'post_user.html', context)

