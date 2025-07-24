from django.shortcuts import render,redirect
from .models import News
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

def homepage(request):
    news_list = News.objects.all().order_by('-created_at')
    return render(request, 'homepage.html', {'news_list': news_list})

def category_news(request, category):
    news_list = News.objects.filter(category=category).order_by('-created_at')
    return render(request, 'category_news.html', {'news_list': news_list, 'category': category})
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home or dashboard
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            login(request, user)
            return redirect('login')

    return render(request, 'register.html')