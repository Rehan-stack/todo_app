from django.contrib import admin
from django.urls import path,include

from todo.views import*


urlpatterns = [
    path('', todolist),

    
]
