from django.forms import ModelForm
from .models import Venue, Events
from django import forms
from datetime import date

today = date.today()

class VenueForm(ModelForm):

    class Meta:

        #zip_code    = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Zipcode'}),label='')

        model = Venue
        fields = ['venue_name', 'venue_address', 'venue_phone', 'venue_website','venue_email']
        #fields = "__all__"
        widgets = { 'venue_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Venue name'}),
                   'venue_address' : forms.TextInput(attrs={'class':'form-control','placeholder':'Venue Address'}),
                   'venue_phone' : forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}),
                   'venue_website' : forms.URLInput(attrs={'class':'form-control','placeholder':'Website'}),
                   'venue_email' : forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
                   }
        labels = {
                'venue_name':'',
                'venue_address': '',
                'venue_phone':'',
                'venue_website': '',
                'venue_email':'',
        }


class EventForm(ModelForm):
    event_date = forms.DateField(widget=forms.TextInput(attrs={'min': today, 'value': today, 'type': 'date','class':'form-control'}), required=True)
    class Meta:
        model = Events
        fields = ['event_name','event_date','venue','desc', 'attendees']
        widgets ={
            'event_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Event Name'}),
            #'event_date': forms.DateInput(attrs={'class':'form-control','placeholder':'Event Date'})
            'venue': forms.TextInput(attrs={'class':'form-control','placeholder':'Venue'}),
            'desc':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),
            'attendees':forms.SelectMultiple(attrs={'class':'form-control','placeholder':'Attendees'})

        }