from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.
class carAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}"  width="40"/>'.format(object.car_photo.url))
    thumbnail.Short_description = 'car photo'
    list_display=["id","thumbnail","car_title","city","color","model","body_style","fuel_type","is_featured","year"]
    list_display_links=["id","thumbnail","car_title"]
    list_editable = ["is_featured"]
    search_fields=["car_title","model","body_style","color","city","year"]
    list_filter = ["car_title","color","city","fuel_type","model","body_style"]

admin.site.register(Car,carAdmin)