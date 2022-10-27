from django.urls import path
from . import views
from cars.views import car_detail,search

app_name = 'pages'

urlpatterns = [
    
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact'),
    path('privacy/',views.privacy_policy,name='privacy'),
    #this is for searching and car_details
    path('<int:id>/',car_detail,name='car_detail'),
    path('search/',search,name='search'),
    #this is for login and register forms#
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
]
