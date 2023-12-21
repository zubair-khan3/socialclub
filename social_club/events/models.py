from django.db import models
from django.contrib.auth.models import User
from datetime import date


from django.core.validators import RegexValidator

# Create your models here.
class Venue(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(blank=True, max_length=200)
    venue_name = models.CharField(max_length=255)
    venue_address= models.CharField(max_length=500)
    venue_phone  = models.CharField(max_length=200) 
    venue_website = models.URLField(blank=True)
    venue_email   = models.EmailField()
    venue_image = models.ImageField(null=True,blank=True, upload_to='images/venue')

    def __str__(self):
        return self.venue_name + ", " + self.venue_address

class VenueImages(models.Model):
    venue_pointer = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE, related_name='venueimage')
    venue_images = models.ImageField(null=True, blank=True,upload_to='media/venue')


class Events(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(blank=True, max_length=200) 
    event_date = models.DateTimeField(null=True)
    event_name = models.CharField( max_length=50)
    venue      = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager    = models.CharField( max_length=50,blank=True, null=True)
    desc       = models.TextField(blank=True)
    attendees = models.ManyToManyField(User, blank=True, related_name='club_members')

    def __str__(self):
        return self.event_name + ', ' + self.created_by
    
    class meta:
        readonly_fields=('manager', )

    @property
    def till_date(self):
        date_remain = ''
        today_date = date.today()
        
        current_year = int(date.today().strftime('%y'))
        
        current_month = int(date.today().strftime("%m"))
        current_day = int(date.today().strftime("%d"))

        event = self.event_date.date() #getting event date
        
        event_year = int(event.strftime("%y"))
        event_month = int(event.strftime("%m"))
        event_day = int(event.strftime("%d"))
       

        if event_year  > current_year:
            #date_remain = str(event_month).split(',',1)[0]
            
            date_remain = 'future'
        if current_year == event_year:
            if current_month  >  event_month:
                date_remain = "Occured"
                
            elif current_month  ==  event_month:
                date_remain = 'this month'
        
            elif current_month  <   event_month:
                date_remain = 'future'
        if current_year > event_year:
            date_remain= "occured"
            
        return date_remain
    
    @property
    def date_remain(self):
        today = date.today()
        date_remain = self.event_date.date() - today
        if self.event_date.date() > today:
            days = 'future'
            date_remain = str(date_remain).split(',',1)[0]
        else:
            days='past'

        return days


class GenderChoice(models.TextChoices):
    FEMALE = 'F', 'Female'
    MALE = 'M', 'Male'
   


class UserDetails(models.Model):
    user_info = models.ForeignKey(User, blank=True,null=True, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GenderChoice.choices, null=True)
    user_city = models.CharField(max_length=50,blank= True, null=True)
    user_state = models.CharField(max_length=50,blank=True,null=True)
    user_country = models.CharField(max_length=100,blank=True,null=True,default="Not Defined")
    user_number = models.CharField(max_length=20, validators=[RegexValidator(regex='^(\+?\d{1,3})?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')])
    user_picture = models.ImageField(null=True,blank=True, upload_to='images/' ,default="images/default_profile_picture.png")


class CarouselImages(models.Model):
    title =  models.CharField(max_length=255, null=True, blank=True)
    summary = models.CharField(max_length=500, null=True, blank=True)
    carousel_images = models.ImageField(null=True, blank=True,upload_to='media/carousel')
