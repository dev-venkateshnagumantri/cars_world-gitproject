from django.shortcuts import render,redirect
from .models import Team
from cars.models import Car
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contact
from cars.models import Car
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

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
        'body_style_search':body_style_search
    }
    return render(request,'pages/home.html',context=data)

def about(request):
    data = {
        'Team' : Team.objects.all()
    }
    return render(request,'pages/about.html',context=data)

def  services(request):
    return render(request,'pages/services.html')

def privacy_policy(request):
    return render(request,'pages/privacy.html')

def contact(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            subject = request.POST['subject']
            phone = request.POST['phone']
            message = request.POST['message']

            #customizing the email
            contact_subject = 'Some user is trying to contact you in carzone website regarding '+subject

            message_body = 'Name: '+first_name+' '+last_name+'\nEmail Adress: '+email+'\nphone: '+phone+'\nmessage: '+message

            #sending emails part
            admin_emails = []
            admin_info = User.objects.filter(is_superuser = True)
            for item in admin_info:
                admin_emails.append(item.email)

            send_mail(
                contact_subject,
                message_body,
                'developervenkatesh2001@gmail.com',
                admin_emails,
                fail_silently=False,
            )

            messages.success(request,"Thanks for contacting us. we will get back to you shortly.")
            return redirect('pages:contact')
        else:
            messages.error(request,"You must be logged in before Contacting us!")
            return redirect('pages:login')
    
    
    return render(request,'pages/contact.html')

#for login and register activities#   
def login(request):
    if request.method=='POST':
        field=request.POST['field']
        password=request.POST['password']
        user = auth.authenticate(username=field, password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now Logged in.')
            return redirect('pages:dashboard')
        try:
            email_found = User.objects.get(email=field.lower())
        except:
            messages.error(request,'Invalid Login Credentials !')
            return redirect('pages:login')

        username = email_found.username
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now Logged in.')
            return redirect('pages:dashboard')
        else:
            messages.error(request,'Invalid Login Credentials !')
            return redirect('pages:login')
    else:
        return render(request,'pages/login.html')

def register(request):

    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already exists, Try using different one ! ')
                return redirect('pages:register')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'OOPS! entered email already exists, Try another one.')
                return redirect('pages:register')
            else:
                user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                user.save()
                auth.login(request,user,backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request,'You are successfully registered and logged in !')
                return redirect('pages:dashboard')
        else:
            messages.error(request,'password and confirm password fields do not match !')
            return redirect('pages:register')
    else:
        return render(request,'pages/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are successfully logged out !')
    return redirect('pages:login')

@login_required(login_url = 'pages:login')
def dashboard(request):
    user_inquiry = Contact.objects.all().order_by('-created_date').filter(user_id = request.user.id)
    data = {
        'inquiries' : user_inquiry,
        
    }
    return render(request,'pages/dashboard.html',context=data)