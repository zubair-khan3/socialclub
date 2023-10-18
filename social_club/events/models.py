from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Venue(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(blank=True, max_length=200)
    venue_name = models.CharField(max_length=255)
    venue_address= models.CharField(max_length=500)
    venue_phone  = models.CharField(max_length=200) 
    venue_website = models.URLField(blank=True)
    venue_email   = models.EmailField()

    def __str__(self):
        return self.venue_name + ", " + self.venue_address




class Events(models.Model):
    created_on = models.DateTimeField( auto_now_add=True)
    created_by = models.CharField(blank=True, max_length=200) 
    event_date = models.DateTimeField(null=True)
    event_name = models.CharField( max_length=50)
    venue      = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager    = models.CharField( max_length=50,blank=True, null=True)
    desc       = models.TextField(blank=True)
    attendees = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.event_name + ', ' + self.created_by
    
    class meta:
        readonly_fields=('manager', )

