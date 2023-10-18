from django.forms import ModelForm
from .models import Venue
from django import forms

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