from django.contrib import admin
from .models import Venue, Events
# Register your models here.
admin.site.register(Venue)

#admin.site.register(Events)


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'event_date')
    ordering = ('created_on',)
    search_fields = ('event_name', 'venue',)