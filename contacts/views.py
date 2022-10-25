from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.
def inquiry(request):
    if request.method=='POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        car_id = request.POST['car_id']
        customer_need = request.POST['customer_need']
        car_title = request.POST['car_title']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message =  request.POST['message']
        user_id =  request.POST['user_id']
        if user_id == "0":
            messages.error(request,"you must be logged in inorder to inquire about a specific car !")
            return redirect("pages:login")
        else:
            if request.user.is_authenticated:
                user_id = request.user.id
                has_contacted = Contact.objects.all().filter(car_id=car_id,user_id=user_id)
                if has_contacted:
                    messages.error(request,"you already filed inquiry about this car.please be patient until we get back to you!")
                    return redirect("/"+car_id) 
            contact = Contact(first_name=firstname,last_name=lastname,car_id=car_id,customer_need=customer_need,
            car_title=car_title,city=city,state=state,email=email,phone=phone,message=message,user_id=user_id)
            #here sending emails part#
            admin_emails = []
            admin_info = User.objects.filter(is_superuser = True)
            for item in admin_info:
                admin_emails.append(item.email)
            send_mail(
                'New Car inquiry about car '+car_title+' check here.',
                'Heyy! admin. You got a new car inquiry about car '+car_title+'.please login to admin panel for more info. this inquiry is setup by '+firstname+' '+lastname+' send him/her feedback as soon as possible.',
                'developervenkatesh2001@gmail.com',
                admin_emails,
                fail_silently=False,
            )
            
            contact.save()
            messages.success(request,"your request has been submitted, we will get back to you shortly.")
            return redirect("/"+car_id)

