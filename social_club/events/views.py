from django.shortcuts import render,redirect, HttpResponse
import calendar
from calendar import HTMLCalendar
from datetime import datetime

from .models import Events, Venue, UserDetails, VenueImages, CarouselImages 

from .forms import VenueForm, EventForm, UserDetailsForm, VenueImageForm
from django.contrib import messages
from django.core.paginator import Paginator
import csv 
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from dateutil.relativedelta import relativedelta #pip install python-dateutil
from datetime import date
from django.db.models.functions import Trunc




today = datetime.today()
current_month = today.strftime("%B")


# Create your views here.

def index(request, month=current_month ,year=datetime.now().year):
    events = Events.objects.order_by('-created_on')[:10]
    venues = Venue.objects.order_by('-created_on')[:10]
    
    carousel = CarouselImages.objects.all()
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
                  'current_time':current_time, 
                  'carousel':carousel,
                  'events': events,
                  'venues': venues})



#--------------------------- VENUE -------------------------------------------------

def add_venue(request):    
    form = VenueForm() #Venue information
    image_form = VenueImageForm() #for images.
    if request.user.is_authenticated:
        if request.method == "POST":
            form = VenueForm(request.POST)
    
            if form.is_valid():
                form_save = form.save(commit=False)
                form_save.created_by = request.user
                form_save.save()
                for uploaded_file in request.FILES.getlist('files'):
                    print(uploaded_file)
                    VenueImages.objects.create(venue_pointer = form_save, venue_images =uploaded_file)
                messages.success(request,"Data submitted successfully")
                return redirect('index')
            else:
                print(form_save.errors)
    return render(request,'events/add_venue.html',{'form':form, 'image_form': image_form})

def update_venue(request,pk):
    user_data = Venue.objects.get(id=pk)
    current_images = VenueImages.objects.filter(venue_pointer = user_data.id)
    
    if request.user.is_authenticated:
        form = VenueForm(request.POST or None ,instance=user_data)
        image = VenueImageForm(request.POST or None , use_required_attribute=False)
        
        if request.method == 'POST':
            if form.is_valid():
                form_save = form.save(commit=False)
                form_save.save()      
                for uploaded_file in request.FILES.getlist('files'):
                    VenueImages.objects.create(venue_pointer = form_save, venue_images =uploaded_file)
                messages.success(request,"Data Updated")
                return redirect('index')
    return render(request,'events/update_venue.html',{'form':form, 'image':image})



def all_venues(request): 
    contact_list = Venue.objects.all().order_by('-created_on')
    images = VenueImages.objects.all()
    paginator = Paginator(contact_list, 5)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'events/all_venues.html',{'page_obj':page_obj, 'images':images})


def search_venue(request):
    if request.method == 'POST':
        searched = request.POST['search']
        if searched == "":
            messages.success(request,"Please search something")
            return render(request,'events/venue_result.html',{'search':searched})
        if searched != "": 
            images = VenueImages.objects.all() 
            venue_search = Venue.objects.filter(venue_name__icontains=searched)
            return render(request,'events/venue_result.html',{'venue_search':venue_search, 
                                                    'searched' :searched, 'images':images})
    else:
        return render(request,'events/venue_result.html',{'search':searched})

def delete_venue(request,pk):
    if request.user.is_authenticated:
        data_id = Venue.objects.get(id=pk)
        if request.user.username == data_id.created_by:
            print(data_id.id)
            return render(request,'events/delete_venue.html',{'data_id':data_id})   
    messages.success(request,'you are not authorized')
    return redirect('all_venues')


def confirm_delete_venue(request,pk):
    if request.user.is_authenticated:
        event_data = Venue.objects.get(id=pk)
        event_data.delete()
        messages.success(request,"Venue data deleted.!")
        return redirect('all_venues')
    
def venue_csv(request):
    if request.user.is_authenticated:
        response = HttpResponse(content_type = 'text/plain')
        response['content-disposition'] = 'attachment; filename=venue.csv'
        writer = csv.writer(response)
        venues = Venue.objects.all()
        writer.writerow(["Venue Name", "Venue Address", "Phone", "Website","email"])
        for data in venues:
            writer.writerow([data.venue_name,data.venue_address,data.venue_phone,data.venue_website, data.venue_email])
        return response
    else:
        messages.success(request,'you need to login..')
        return redirect('user_login')
    
#----------------------------------------------------------------------------------------------------------

#--------------------------- EVENTS -----------------------------------------------------------------------

    
def all_events(request):
    contact_list = Events.objects.all().order_by('-created_on')
    paginator = Paginator(contact_list, 5)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request,'events/all_events.html',{ "page_obj": page_obj})

def add_event(request):
    form = EventForm
    if request.user.is_authenticated:
        if request.method == "POST":
            form = EventForm(request.POST)
            if form.is_valid():
                form_save = form.save(commit=False)
                form_save.created_by = request.user
                form_save.manager = request.user
                form_save.save()
                messages.success(request,"Event Added Successfully..")
                return redirect("index")
    return render(request,'events/add_event.html',{'form':form})

def search_event(request):
    if request.method == 'POST':
        searched = request.POST['search']
        if searched == "":
            messages.success(request,"Please search something")
            return render(request,'events/event_result.html',{'search':searched})
        if searched != "":           
            event_search = Events.objects.filter(event_name__icontains=searched) 
            return render(request,'events/event_result.html',{ 'event_search':event_search,'searched' :searched})
    else:
        return render(request,'events/event_result.html',{'search':searched})

def update_event(request,pk):
    user_data = Events.objects.get(id=pk)
    if request.user.is_authenticated:
       form = EventForm(request.POST or None,instance=user_data)
       if form.is_valid():
           form.save()
           messages.success(request,'Data Updated')
           return redirect('all_events')
    return render(request, 'events/update_event.html',{'form': form})


def delete_event(request,pk):
    if request.user.is_authenticated:
        data_id = Events.objects.get(id=pk)
        if request.user.username ==  data_id.manager:
            return render(request,'events/delete_event.html',{'data_id':data_id})
    messages.success(request,'you are not authorized')
    return redirect('all_events')



def confirm_delete_event(request,pk):
    if request.user.is_authenticated:
        event_data = Events.objects.get(id=pk)
        if request.user.username ==  event_data.manager:
            event_data.delete()
            messages.success(request,"Event data deleted.!")
            return redirect('all_events')
    messages.success(request,'you are not authorized')
    return redirect('all_events')

def event_csv(request):
    if request.user.is_authenticated:
        response = HttpResponse(content_type = 'text/plain')
        response['content-disposition'] = 'attachment; filename=event.csv'
        writer = csv.writer(response)
        events = Events.objects.all()
        writer.writerow(["Event Name", "Event date", "Event Venue", "Event manager","Description","Attendees"])
        for data  in events:
            d = data.attendees.all()
            for i in d:
                print(i)
            writer.writerow([data.event_name, data.event_date, data.venue,data.manager, data.desc, data.attendees])
        return response
    else:
        messages.success(request,'you need to login..')
        return redirect('user_login')

#------------------------------------------------------------------------------------------- 

#-------------------- USER ------------------------------------------------------------------

def user_profile(request,name):
    print(name)
    if request.user.is_authenticated:
        user_data = User.objects.get(username= request.user.username)
        user_detail = UserDetails.objects.get(user_info = request.user.id)
        return render(request,'events/user_profile.html', {'user_data':user_data,'user_detail':user_detail})
    messages.success(request,"you need to login")
    return redirect('index')


def update_user(request, name):    
    form = UserDetailsForm()
    if request.user.is_authenticated:
        user_data = UserDetails.objects.get(user_info = request.user.id)        
        form = UserDetailsForm(request.POST or None, request.FILES or None, instance=user_data)        
        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.user_info  = request.user
            form.save()
            messages.success(request,"Data Updated")
            return redirect('index')
    return render(request, 'events/update_user.html',{'form':form})

# events created by individual user.
def user_events(request,name):
    if request.user.is_authenticated:
        user_data = Events.objects.filter(created_by =name)

        return render(request,'events/user_events.html',{'user_data':user_data})
    messages.success(request,'you need to login')
    return redirect('index')

def user_venues(request,name):
    if request.user.is_authenticated:
        user_data = Venue.objects.filter(created_by =name)
        images = VenueImages.objects.all()
        return render(request,'events/user_venues.html',{'user_data':user_data,'images':images})
    messages.success(request,'you need to login')
    return redirect('index')
