from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login,logout
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def frontpage(request):
    return render(request, 'frontpage.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            messages.error(request, "Passwords didn't match!")
            return redirect('signup')
        
        try:
            user = User.objects.create_user(username=username, password=password1)
            return redirect('login')
        except Exception as e:
            messages.error(request, "Username already exists or invalid input!")
            return redirect('signup')
            
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('rooms')
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('login')
            
    return render(request, 'login.html')
def logoutfromchat(request):
    logout(request)
    return redirect('frontpage')
def about(request):
    return render(request, 'about.html')
def features(request):
    return render(request, 'features.html')
def contact(request):
    return render(request, 'contact.html')

@login_required
def rooms(request):
    rooms = Room.objects.all().order_by('name')
    return render(request, 'rooms.html', {'rooms': rooms})
@login_required
def room(request,slug):
    room = Room.objects.get(slug=slug)
    return render(request, 'room.html', {'room': room})
