from django.shortcuts import render,get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
# Create your views here.

def cars(request):
    all_cars = Car.objects.all().order_by('-created_date')

    model_search = Car.objects.values_list('model',flat=True).distinct()
    city_search = Car.objects.values_list('city',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct().order_by('year')
    body_style_search = Car.objects.values_list('body_style',flat=True).distinct()

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
        'model_search':model_search,
        'city_search' : city_search,
        'year_search' : year_search,
        'body_style_search':body_style_search
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

def search(request):
    cars_list= Car.objects.all().order_by('-created_date')

    car_title_search = Car.objects.values_list('car_title',flat=True).distinct()
    model_search = Car.objects.values_list('model',flat=True).distinct()
    city_search = Car.objects.values_list('city',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct().order_by('year')
    body_style_search = Car.objects.values_list('body_style',flat=True).distinct()
    engine_search = Car.objects.values_list('engine',flat=True).distinct()
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars_list = cars_list.filter(description__icontains=keyword)
    
    if 'car_title' in request.GET:
        car_title = request.GET['car_title']
        if car_title:
            cars_list = cars_list.filter(car_title__iexact=car_title)
    
    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars_list = cars_list.filter(model__iexact=model)
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars_list = cars_list.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars_list = cars_list.filter(year__iexact=year)
    
    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars_list = cars_list.filter(body_style__iexact=body_style)

    if 'engine' in request.GET:
        engine = request.GET['engine']
        if engine:
            cars_list = cars_list.filter(engine__iexact=engine)

    if 'min_price' in request.GET:        
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars_list = cars_list.filter(price__gte=min_price,price__lte=max_price)

    car_title_search = Car.objects.values_list('car_title',flat=True).distinct()
    model_search = Car.objects.values_list('model',flat=True).distinct()
    city_search = Car.objects.values_list('city',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct().order_by('year')
    body_style_search = Car.objects.values_list('body_style',flat=True).distinct()
    engine_search = Car.objects.values_list('engine',flat=True).distinct()
    #for humanizing indian currency prices of cars
    for item in cars_list :
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
        'searched_cars':cars_list,
        'car_title_search':car_title_search,
        'model_search':model_search,
        'city_search' : city_search,
        'year_search' : year_search,
        'body_style_search':body_style_search,
        'engine_search' : engine_search,
    }

    return render(request,'cars/search.html',context=data)
