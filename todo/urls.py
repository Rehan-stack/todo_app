from django.contrib import admin
from django.urls import path,include

from todo.views import*


urlpatterns = [

    path('currenttodos', currenttodos,name='currenttodos'),
    path('signup', signup,name='signupuser'),
    path('',home,name='home'),
    path('logout',logoutuser,name='logoutuser'),
    path('login',loginuser,name='loginuser'),
    path('createtodo',createtodo,name='createtodo'),
    path('completedtodo',completedtodo,name='completedtodos'),
    path('viewtodo/<int:todo_pk>',viewtodo,name='viewtodo'),
    path('viewtodo/<int:todo_pk>/complete',completetodo,name='completetodos'),
    path('viewtodo/<int:todo_pk>/delete',deletetodo,name='deletetodos'),

    
]
