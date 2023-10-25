from django.contrib import admin
from .models import Event, Event_Image, Visitor

class EventPanel ( admin.ModelAdmin ) :
    list_display = ['name','user','start_at']
admin.site.register(Event, EventPanel)


class VisitorPanel ( admin.ModelAdmin ) :
    list_display = ['full_name','event','is_arrived']
admin.site.register(Visitor, VisitorPanel)


