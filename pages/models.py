from django.db import models

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='Photos/%Y/%m/%d/')
    linkedin_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    google_plus_link = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.first_name+' '+self.last_name