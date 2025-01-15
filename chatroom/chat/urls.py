from django.urls import path
from .views import *

urlpatterns = [
   path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
]