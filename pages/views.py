from django.shortcuts import render
from .models import Team
# Create your views here.

def home(request):
    data = {
        'Team' : Team.objects.all()
    }
    return render(request,'pages/home.html',context=data)

def about(request):
    data = {
        'Team' : Team.objects.all()
    }
    return render(request,'pages/about.html',context=data)

def  services(request):
    return render(request,'pages/services.html')

def contact(request):
    return render(request,'pages/contact.html')
    
