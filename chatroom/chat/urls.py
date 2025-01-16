from django.urls import path
from .views import *

urlpatterns = [
   path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path("about/", about, name='about'),
    path("features/", features, name='features'),
    path("contact/", contact, name='contact'),
    path("home/", home, name='home'),
    path("logout/",  logoutfromchat, name='logout'),
]