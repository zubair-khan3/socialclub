
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name="index"),
    path('<str:month>/<int:year>/',views.index),
    
    path('all_events',views.all_events,name="all_events"), #user can see all events on webpate url.
    path('all_venues', views.all_venues, name="all_venues"),
    
    path('add_venue', views.add_venue,name="add_venue"),
    path('add_event', views.add_event,name='add_event'),

    
    path('search_venue', views.search_venue, name="search_venue"),
    path('search_event', views.search_event, name="search_event"),
    #path('search_result/<search>', views.search_result,name="search_result"),
    path('update_venue/<int:pk>', views.update_venue, name="update_venue")
    
]

