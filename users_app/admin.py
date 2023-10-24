from django.contrib import admin
from .models import User


class UserPanel ( admin.ModelAdmin ) :
    list_display = ['full_name','email']

admin.site.register(User, UserPanel)