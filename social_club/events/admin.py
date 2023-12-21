from django.contrib import admin
from .models import Venue, Events, UserDetails, VenueImages ,CarouselImages




# Register your models here.
admin.site.register(Venue)

#admin.site.register(Events)


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'event_date')
    ordering = ('created_on',)
    search_fields = ('event_name', 'venue',)


@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('user_info','user_city')
    ordering = ('user_info',)
    search_fields = ('user_info',)


@admin.register(VenueImages)
class VenueImagesAdmin(admin.ModelAdmin):
    list_display=('venue_pointer',)

@admin.register(CarouselImages)
class CarouselImagesAdmin(admin.ModelAdmin):
    list_display=("title",)
    ordering = ('title',)