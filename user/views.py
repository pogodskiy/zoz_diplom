from django.contrib.auth import logout
from post.models import Post
from .forms import RegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def home(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'user/home.html', {'posts': posts})

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


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')#заполнение очищенных форм
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password) #если все нормально, то создается user
            if user is not None:# если user создат, то входим
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')





