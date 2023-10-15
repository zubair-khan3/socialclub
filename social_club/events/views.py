from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime

current_year = datetime.now().year
today = datetime.now()
current_month = today.strftime("%B")


# Create your views here.

def index(request, month=current_month ,year=current_year):

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

