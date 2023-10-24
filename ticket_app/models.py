from django.db import models
from users_app.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from uuid import uuid4

class Event(models.Model) : 
    name = models.CharField(max_length=100)
    start_at = models.DateField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    uuid = models.UUIDField(null=True,blank=True)

    def __str__(self) : 
        return f"{self.name}"
    
class Visitor (models.Model) : 
    full_name = models.CharField(max_length=100)
    picture = models.FileField(upload_to='visitors-images/')
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    uuid = models.UUIDField(null=True,blank=True)
    is_arrived = models.BooleanField(default=False)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)

    def __str__(self) : 
        return f'{self.full_name}'

class Event_Image( models.Model ) :
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    image =models.FileField(upload_to='event-images/')

    def __str__(self) : 
        return f'{self.event.name}'
    

@receiver(post_save, sender = Event)
def Create_Event_Uuid (created, instance, **kwargs) :
    if created :
        instance.uuid = uuid4()
        instance.save()

@receiver(post_save, sender = Visitor)
def Create_Visitor_Uuid (created, instance, **kwargs) :
    if created :
        instance.uuid = uuid4()
        instance.save()