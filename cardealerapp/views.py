from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login/')
def index(request):
    return render(request,'index.html')

def cars(request):
    return render(request,'cars.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def workshop(request):
    return render(request,'workshop.html')

def spareparts(request):
    return render(request,'spareparts.html')
    
def cardetails(request):
    return render(request,'cardetails.html')