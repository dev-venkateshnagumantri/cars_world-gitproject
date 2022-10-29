from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from django.core.validators import MinValueValidator,MaxValueValidator
from cloudinary.models import CloudinaryField
# Create your models here.
class Car(models.Model):
    state_choices=(
        ('AP','Andhra Pradesh'),
        ('AR','Arunachal Pradesh'),
        ('AS','Assam'),
        ('BR','Bihar'),
        ('CH','Chhattisgarh'),
        ('GOA','Goa'),
        ('GJ','Gujarat'),
        ('HAR','Haryana'),
        ('HP','Himachal Pradesh'),
        ('JK','Jammu and Kashmir'),
        ('JD','Jharkhand'),
        ('KAR','Karnataka'),
        ('KER','Kerala'),
        ('MP','Madhya Pradesh'),
        ('MH','Maharashtra'),
        ('MNP','Manipur'),
        ('MEG','Meghalaya'),
        ('MZ','Mizoram'),
        ('NGL','Nagaland'),
        ('ODI','Odisha'),
        ('PUN','Punjab'),
        ('RJ','Rajasthan'),
        ('SK','Sikkim'),
        ('TN','Tamil Nadu'),
        ('TG','Telangana'),
        ('TR','Tripura'),
        ('UP','Uttar Pradesh'),
        ('UT','Uttarakhand'),
        ('WB','West Bengal')

    )
    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    year_choices = []
    for r in range(2000, (datetime.now().year+1)):
        year_choices.append((r,r))

        
    car_title=models.CharField(max_length=100)
    state=models.CharField(choices=state_choices,max_length=100)
    city=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    model=models.CharField(max_length=100)
    year=models.IntegerField(('year'),choices=year_choices)
    condition=models.CharField(max_length=100)
    price=models.IntegerField(validators=[MinValueValidator(100000)])
    description=RichTextField()
    car_photo= CloudinaryField('image')
    car_photo_1= CloudinaryField('image')
    car_photo_2= CloudinaryField('image')
    car_photo_3= CloudinaryField('image')
    car_photo_4= CloudinaryField('image')
    features = MultiSelectField(choices = features_choices)
    body_style=models.CharField(max_length=100)
    engine=models.CharField(max_length=100)
    transmission=models.CharField(max_length=100)
    interior_color=models.CharField(max_length=100)
    miles=models.IntegerField()
    doors=models.CharField(choices=door_choices,max_length=100)
    passengers=models.IntegerField()
    vin_no=models.CharField(max_length=100)
    milege = models.IntegerField()
    fuel_type=models.CharField(max_length=100)
    no_of_owners=models.IntegerField()
    is_featured=models.BooleanField(default=False)
    created_date=models.DateTimeField(default=datetime.now,blank=True)


    def __str__(self):
        return self.car_title
    
    

