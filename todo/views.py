from django.shortcuts import render

# Create your views here.

def  todo(requests):
    return render(requests, 'todolist.html')