from django.contrib import admin
from django.urls import path,include

from todo.views import*


urlpatterns = [

    path('currenttodo', currenttodo,name='currenttodo'),
    path('signup', signup),
    path('',home),
    path('logout',logoutuser,name='logoutuser'),
    path('login',loginuser,name='login')

    
]
