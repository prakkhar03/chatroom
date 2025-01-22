from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login,logout
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

def frontpage(request):
    return render(request, 'frontpage.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            messages.error(request, "Passwords didn't match!")
            return redirect('signup')
        
        try:
            user = User.objects.create_user(username=username,email=email, password=password1)
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
def create_room(request):
    if request.method == 'POST':
        room_name = request.POST.get('room_name', '').strip()
        if room_name:
            slug = slugify(room_name)
            try:
                room = Room.objects.create(name=room_name, slug=slug)
                return redirect('room', slug=room.slug)
            except:
                messages.error(request, "Room name already exists!")
                return redirect('create_room')
    return render(request, 'create_room.html')

@login_required
def room(request, slug):
    room = get_object_or_404(Room, slug=slug)
    context = {
        'room': room,
        'room_name': room.name,
        'room_slug': room.slug,
        'username': request.user.username
    }
    return render(request, 'room.html', context)

@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})
def changepassword(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')
        
        if not request.user.check_password(old_password):
            messages.error(request, "Incorrect old password!")
            return redirect('profile')
        
        if new_password1 != new_password2:
            messages.error(request, "Passwords didn't match!")
            return redirect('profile')
        
        user = request.user
        user.set_password(new_password1)
        user.save()
        
        messages.success(request, "Password changed successfully!")
        return redirect('profile')
    
    return render(request, 'changepassword.html')