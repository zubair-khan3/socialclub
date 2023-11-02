
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
    path('update_venue/<int:pk>', views.update_venue, name="update_venue"),
    path('update_event/<int:pk>',views.update_event,name='update_event'),

    path('delete_venue/<int:pk>',views.delete_venue,name='delete_venue'),
    path('confirm_delete_venue/<int:pk>',views.confirm_delete_venue,name='confirm_delete_venue'),

    path('delete_event/<int:pk>', views.delete_event,name='delete_event'),
    path('confirm_delete_event/<int:pk>', views.confirm_delete_event,name='confirm_delete_event'),
    
    path('venue_csv',views.venue_csv,name="venue_csv"),
    path('event_csv',views.event_csv,name="event_csv")
    
]

