from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('visitor/register/<str:eventuuid>/',views.visitor_register,name='visitor_register'),
]