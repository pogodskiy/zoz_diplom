from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import User
from .forms import RegistrationForm
from post.models import Post
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def home(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'user/home.html', {'posts': posts})



from .forms import RegistrationForm

def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'user/register.html', {'form': form})



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})




def user_logout(request):
    logout(request)
    return redirect('home')


def user_delete(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return True, "Пользователь успешно удален."
    except User.DoesNotExist:
        return False, "Пользователь с указанным ID не найден."


def profile(request,user_id):
    pass

