from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate

# Create your views here.
    
def home(request):
    return render(request, 'home.html')



def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html',{'form':UserCreationForm})

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                 user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                 user.save()
                 login(request,user)
                 return redirect('currenttodo')

            except IntegrityError:
                return render(request, 'signup.html',{'form':UserCreationForm,'error':'username not found'})

        else:
            return render(request, 'signup.html',{'form':UserCreationForm,'error': 'password not same'})

def logoutuser(request):
    if request.method =='POST':
        logout(request)
        return redirect(home)


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'login.html',{'form':AuthenticationForm})
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request, 'login.html',{'form':AuthenticationForm,'error':'username not matching'})
        else:
            login(request,user)
            return redirect('currenttodo')
            


def currenttodo(request):
    return render(request, 'currenttodo.html',)