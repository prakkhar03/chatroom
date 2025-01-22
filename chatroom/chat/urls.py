from django.urls import path
from .views import *

urlpatterns = [
   path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path("about/", about, name='about'),
    path("features/", features, name='features'),
    path("contact/", contact, name='contact'),
    path("logout/",  logoutfromchat, name='logout'),
    path("rooms/", rooms, name='rooms'),
    path("create-room/", create_room, name='create_room'),
    path("room/<slug:slug>/", room, name='room'),
    path("profile/", profile, name='profile'),
    path("newpassword/", changepassword, name='newpassword'),
]