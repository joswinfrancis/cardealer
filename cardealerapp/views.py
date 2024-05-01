from django.shortcuts import render

# Create your views here.
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