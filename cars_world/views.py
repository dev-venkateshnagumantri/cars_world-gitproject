import django

def custom_page_not_found(request,exception):
     return django.views.defaults.page_not_found(request, None)