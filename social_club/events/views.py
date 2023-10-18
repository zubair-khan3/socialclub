from django.shortcuts import render,redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Events, Venue
from .forms import VenueForm
from django.contrib import messages

from django.core.paginator import Paginator


today = datetime.now()
current_month = today.strftime("%B")


# Create your views here.

def index(request, month=current_month ,year=datetime.now().year):

    month = month.capitalize()
    #convert month into number
    month_number = int(list(calendar.month_name).index(month))
    
    cal = HTMLCalendar().formatmonth(year,month_number)
    now = datetime.now()
    current_time =  now.strftime("%m/%d/%Y")
    
    return render(request, 'index.html',
                  {'month':month,
                  'year':year,
                  'cal': cal,
                  'current_time':current_time})


def all_events(request):
    all_events = Events.objects.all()
    return render(request,'events/all_events.html',{'all_events':all_events})

def add_venue(request):
    form = VenueForm
    if request.user.is_authenticated:
        if request.method == "POST":
            form = VenueForm(request.POST)
            if form.is_valid():
                form_save = form.save(commit=False)
                form_save.created_by = request.user
                form_save.save()
                messages.success(request,"Data submitted successfully")
                return redirect('events/add_venue')
    
    return render(request,'events/add_venue.html',{'form':form})


def all_venues(request):
    venues = Venue.objects.all()
    return render(request,'events/all_venues.html',{'venues':venues})


def search_venue(request):

    if request.method == 'POST':
        searched = request.POST['search']
        if searched == "":
            messages.success(request,"Please search something")
            return render(request,'events/search.html',{'search':searched})
        if searched != "":  
            venue_search = Venue.objects.filter(venue_name__icontains=searched)
          

            return render(request,'events/search.html',{'venue_search':venue_search, 
                                                        'searched' :searched})
    else:
        return render(request,'events/search.html',{'search':searched})
    


def search_event(request):

    if request.method == 'POST':
        searched = request.POST['search']
        if searched == "":
            messages.success(request,"Please search something")
            return render(request,'events/search.html',{'search':searched})
        if searched != "":  
            
            event_search = Events.objects.filter(event_name__icontains=searched) 

            return render(request,'events/search.html',{ 'event_search':event_search, 
                                                        'searched' :searched})
    else:
        return render(request,'events/search.html',{'search':searched})

# def search_result(request,search):
#     searched = search
#     print(searched)
#     if request.user.is_authenticated:
#         print("in search_result", search)
#         venue_search = Venue.objects.filter(venue_name__icontains=searched)
#         event_search = Events.objects.filter(event_name__icontains=searched)

#     return render(request,'events/search.html',{})


def update_venue(request,pk):
    user_id = pk
    return render(request,'events/update_venue.html',{'user_id':user_id})