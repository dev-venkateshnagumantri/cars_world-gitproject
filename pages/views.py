from django.shortcuts import render
from .models import Team
from cars.models import Car
from heapq import *
# Create your views here.

def home(request):

    featured_cars=Car.objects.all().order_by('created_date','-price').filter(is_featured=True)
    totalcars_list = Car.objects.all().order_by('-created_date')

    model_search = Car.objects.values_list('model',flat=True).distinct()
    city_search = Car.objects.values_list('city',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct().order_by('year')
    body_style_search = Car.objects.values_list('body_style',flat=True).distinct()
    
    #for humanizing indian currency price of featured cars
    for item in featured_cars:
        prc=str(item.price)
        lastprc = prc[-3:]
        firstprc=prc[ :-3]
        firstprc=firstprc[::-1]
        s=""
        for i in range(len(firstprc)):
            if i!=0 and i%2==0:
                s=s+','+firstprc[i]
            else:
                s=s+firstprc[i]
        s=s[::-1]
        prc=s+','+lastprc
        item.price = prc

    #for humanizing indian currency price of all cars   
    for item in totalcars_list:
        prc=str(item.price)
        lastprc = prc[-3:]
        firstprc=prc[ :-3]
        firstprc=firstprc[::-1]
        s=""
        for i in range(len(firstprc)):
            if i!=0 and i%2==0:
                s=s+','+firstprc[i]
            else:
                s=s+firstprc[i]
        s=s[::-1]
        prc=s+','+lastprc
        item.price = prc

    data = {
        'Team' : Team.objects.all(),
        'featured_cars': featured_cars,
        'all_cars' : totalcars_list,

        'model_search':model_search,
        'city_search' : city_search,
        'year_search' : year_search,
        'body_style_search':body_style_search,
        

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
    
