from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from .models import profile, library
from store.models import Cart
from homepage.views import getcart

# Create your views here.
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    Profile = profile.objects.get(user=request.user)
    games = library.objects.get(profile=Profile).games.all()
    cart = getcart(request)
    return render(request, 'dashboard.html', {'profile': Profile, 'games': games, 'cart': cart})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, 'Invalid username or password')
                return render(request, 'login.html', {'form': form})
            login(request, user)
            return redirect('dashboard')
    else:
        form = LoginForm()
    cart = getcart(request)
    return render(request, 'login.html', {'form': form, 'cart': cart})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                messages.error(request, 'This username is already taken')
                return redirect('register')
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if profile.objects.filter(user=user).exists():
                messages.error(request, 'This user already exists')
                return redirect('register')
            profile.objects.create(
                user=user,
                displayname=form.cleaned_data['displayname']
            )
            library.objects.create(
                profile=profile.objects.get(user=user)
            )
            Cart.objects.create(
                user=profile.objects.get(user=user),
            )

            return redirect('login')
    else:
        form = RegistrationForm()

    cart = getcart(request)
    return render(request, 'register.html', {'form': form, 'cart': cart})