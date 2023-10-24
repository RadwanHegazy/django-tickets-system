from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class User (AbstractUser):
    username = None
    groups = None
    first_name = None
    last_name = None


    full_name = models.CharField(_('Full Name'),max_length=100)
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['full_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.full_name
    
    def login (**kwargs) : 
        email = kwargs['email']
        password = kwargs['password']

        user = User.objects.filter(email=email)
        
        response = {
            'errors':''
        }

        if not user.exists() or user.count() > 1 :
            response['errors'] = 'خطأ في البريد الالكتروني'
            return response
        
        user = user.first()

        if not user.check_password(password) :
            response['errors'] = 'خطأ في كلمة السر'
            return response
        
        response['user'] = user

        return response
    