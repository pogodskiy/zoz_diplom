from django.shortcuts import render, redirect, get_object_or_404
from post.forms import PostForm
from django.contrib.auth.decorators import login_required
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
            return redirect('home')
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
