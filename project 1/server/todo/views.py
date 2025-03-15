from django.shortcuts import render, redirect
from .forms import LoginForm
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout


@login_required
def home(request):
    return render(request,'home.html')
# Create your views here.
def home2(request):
    return render(request,'home2.html')


@login_required
def login2(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to the homepage
    else:
        form = LoginForm()
    return render(request, 'home', {'form': form})


def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
    else:
        form = SignupForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login') 
    
