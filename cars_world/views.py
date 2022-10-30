<<<<<<< HEAD
import django

def custom_page_not_found(request,exception):
=======
import django

def custom_page_not_found(request,exception):
>>>>>>> c1fe6d6fd59363b222f52a4e4f621e67e554befd
     return django.views.defaults.page_not_found(request, None)