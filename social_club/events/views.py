from django.shortcuts import render,redirect, HttpResponse
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Events, Venue
from .forms import VenueForm, EventForm
from django.contrib import messages
from django.core.paginator import Paginator
import csv 
from django.contrib.auth.models import User
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
    contact_list = Events.objects.all().order_by('-created_on')
    paginator = Paginator(contact_list, 5)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request,'events/all_events.html',{ "page_obj": page_obj})

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
                return redirect('index')
    
    return render(request,'events/add_venue.html',{'form':form})


def add_event(request):
    form = EventForm
    if request.user.is_authenticated:
        if request.method == "POST":
            form = EventForm(request.POST)
            if form.is_valid():
                form_save = form.save(commit=False)
                form_save.created_by = request.user
                form_save.save()
                messages.success(request,"Event Added Successfully..")
                return redirect("index")
    return render(request,'events/add_event.html',{'form':form})



def all_venues(request):
    contact_list = Venue.objects.all().order_by('-created_on')
    paginator = Paginator(contact_list, 5)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    return render(request,'events/all_venues.html',{'page_obj':page_obj})


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
    user_data = Venue.objects.get(id=pk)
    
    if request.user.is_authenticated:
        
            form = VenueForm(request.POST or None ,instance=user_data)
            if form.is_valid():
                form.save()
                messages.success(request,"Data Updated")
                return redirect('index')
    return render(request,'events/update_venue.html',{'form':form})


def update_event(request,pk):
    user_data = Events.objects.get(id=pk)
    if request.user.is_authenticated:
       form = EventForm(request.POST or None,instance=user_data)
       if form.is_valid():
           form.save()
           messages.success(request,'Data Updated')
           return redirect('index')
    return render(request, 'events/update_event.html',{'form': form})


def delete_event(request,pk):
    data_id = Events.objects.get(id=pk)
    print(data_id.id)
    return render(request,'events/delete_event.html',{'data_id':data_id})

def confirm_delete_event(request,pk):
    if request.user.is_authenticated:
        event_data = Events.objects.get(id=pk)
        event_data.delete()
        messages.success(request,"Event data deleted.!")
        return redirect('all_events')
    



def delete_venue(request,pk):
    data_id = Venue.objects.get(id=pk)
    print(data_id.id)
    return render(request,'events/delete_venue.html',{'data_id':data_id})

def confirm_delete_venue(request,pk):
    if request.user.is_authenticated:
        event_data = Venue.objects.get(id=pk)
        event_data.delete()
        messages.success(request,"Venue data deleted.!")
        return redirect('all_events')
    


def venue_csv(request):
    response = HttpResponse(content_type = 'text/plain')
    response['content-disposition'] = 'attachment; filename=venue.csv'

    writer = csv.writer(response)

    venues = Venue.objects.all()
    writer.writerow(["Venue Name", "Venue Address", "Phone", "Website","email"])


    for data in venues:
        writer.writerow([data.venue_name,data.venue_address,data.venue_phone,data.venue_website, data.venue_email])

    return response


def event_csv(request):
    response = HttpResponse(content_type = 'text/plain')
    response['content-disposition'] = 'attachment; filename=event.csv'

    writer = csv.writer(response)

    events = Events.objects.all()

    writer.writerow(["Event Name", "Event date", "Event Venue", "Event manager","Description","Attendees"])

    
    #e = Events.objects.get(pk=3)
    #print(" attendees ",e.attendees.all())
  
                            
    for data  in events:
        print('id', data.id)
        d = data.attendees.all()
        for i in d:
            print(i)
        writer.writerow([data.event_name, data.event_date, data.venue,data.manager, data.desc, data.attendees])
        
    return response
