from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from todo.forms import*

# Create your views here.

def  todo(request):
    if request.method == "GET":
        all_task = tasklist.objects.all
        return render(request, 'todolist.html',{'all_task':all_task})
    else:
        form = Taskform(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('todolist')
    


def todolist(request):
     all_task = tasklist.objects.all
     return render(request, 'todolist.html',{'all_task':all_task})