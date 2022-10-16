from django.shortcuts import render,get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
# Create your views here.

def cars(request):
    all_cars = Car.objects.all().order_by('-created_date')
    for item in all_cars :
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

    page=request.GET.get('page')
    paged_cars = Paginator(all_cars,4).get_page(page)
    cars_list={
        'cars': paged_cars,
    }
    return render(request,'cars/cars.html',context= cars_list)

def car_detail(request,id):
    single_car = get_object_or_404(Car,pk=id)
    prc = str(single_car.price)
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
    single_car.price = prc

    data = {
        'car_data' : single_car
    }
    return render(request,'cars/car_detail.html', context=data)
