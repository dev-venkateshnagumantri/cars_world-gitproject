from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('',views.home,name='home')
]
