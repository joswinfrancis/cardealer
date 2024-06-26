from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate,login as authlogin,logout as authlogout
# Create your views here.

def login(request):
    error_message=None
    if request.POST:
        username =  request.POST['username']
        password =  request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            authlogin(request,user)
            return redirect('index')
        else:
            error_message='invalid credentials'
    return render(request,'login.html',{'error_message':error_message})

def logout(request):
    authlogout(request)
    return redirect('login')
    

def register(request):
    user=None
    error_message=None
    if request.POST:
        username =  request.POST['username']
        password =  request.POST['password']
        try:
            user=User.objects.create_user(username=username,password=password)
            return redirect('login')
        except Exception as e:
            error_message='invalid credentials'
    return render(request,'register.html',{'user':user,'error_message':error_message})