from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'pages/home.html')

def about_page(request):
    return render (request,'pages/about.html')

def services_page(request):
    return render (request,'pages/service.html')

def contact_page(request):
    return render (request,'pages/contact.html')