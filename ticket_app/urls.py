from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('event/create/',views.create_event,name='create_event'),
    path('event/details/<str:eventuuid>/',views.event_details,name='event_details'),
]