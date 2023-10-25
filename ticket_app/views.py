from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event, Event_Image, Visitor



@login_required
def home (request) : 
    events = Event.objects.filter(user=request.user)

    return render(request,'home.html',{'events':events})



@login_required
def create_event (request) : 

    if request.method == "POST" : 
        event_name = request.POST['event_name']
        start_at = request.POST['start_at']
        user = request.user

        event = Event.objects.create(
            name = event_name,
            start_at = start_at,
            user = user,
        )

        if 'img' in request.FILES :
            images = request.FILES.getlist('img')

            for image in images :
                Event_Image.objects.create(
                    event = event,
                    image = image
                ).save()

        
        return redirect('home')



    return render(request,'create-event.html')


@login_required
def event_details (request, eventuuid) : 
    
    event = get_object_or_404(Event,uuid=eventuuid)

    context = {
        'event' : event,
        'visitors' : Visitor.objects.filter(event=event)
    }

    return render(request,'event-details.html',context)