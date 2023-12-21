from django.forms import ModelForm
from .models import Venue, Events , UserDetails , VenueImages
from django import forms
from datetime import date

from multiupload.fields import MultiFileField

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


# class VenueImageForm(ModelForm):
#     image = MultiFileField(min_num=1, max_num=10)
#     class Meta:
#         model = VenueImages
#         fields = ['venue_images']


#================================================================================


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class VenueImageForm(forms.Form):
    files = MultipleFileField()



#=================================================================================









class EventForm(ModelForm):
    #event_date = forms.DateField(widget=forms.TextInput(attrs={'min': today, 'value': today, 'type': 'date','class':'form-control'}), required=True)
    class Meta:
        model = Events
        fields = ['event_name','event_date','venue','desc', 'attendees']
        widgets ={
            'event_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Event Name'}),
            'event_date': forms.DateInput(attrs={'class':'form-control','placeholder':'Event Date'}),
            'venue': forms.Select(attrs={'class':'form-control','placeholder':'Venue'}),
            'desc':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),
            'attendees':forms.SelectMultiple(attrs={'class':'form-control','placeholder':'Attendees'})

        }
        labels={
            'event_date':'YYYY-MM-DD'
        }


class UserDetailsForm(ModelForm):

    class Meta:
        model = UserDetails
        fields= ['gender','user_city', 'user_state','user_country','user_number','user_picture']

    
        widgets ={
            'gender': forms.Select(attrs={'class':'form-control','placeholder':'Gender'}),
            'user_city': forms.TextInput(attrs={'class':'form-control','placeholder':'City'}),
            'user_state': forms.TextInput(attrs={'class':'form-control','placeholder':'State'}),
            'user_country': forms.TextInput(attrs={'class':'form-control','placeholder':'Country'}),
            'user_number':forms.TextInput(attrs={'class':'form-control','placeholder':'Number'})

        }


