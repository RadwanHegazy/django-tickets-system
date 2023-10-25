from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from ticket_app.models import Event, Event_Image, Visitor
from users_app.models import User
from django.contrib.auth.views import auth_login

def login (request) :

    context = {}

    if request.method == "POST" : 
        email = request.POST['email']
        password = request.POST['password']
        
        u = User.login(email=email,password=password)

        if u['errors'] :
            context = {'error':u['errors']}
        else:
            auth_login(request,u['user'])
            return redirect('home')

    return render(request,'login.html', context)


def register(request) : 

    if request.method == "POST" :
        full_name = request.POST['full_name']
        email = request.POST['email']
        password = request.POST['password']

        u = User.objects.create_user(
            full_name = full_name,
            email = email,
            password = password,
        )

        u.save()

        auth_login(request,u)

        return redirect('home')


    return render(request,'register.html')



def visitor_register (request, eventuuid) : 
    event = get_object_or_404(Event,uuid=eventuuid)
    event_images = Event_Image.objects.filter(event=event)


    context = {
        'event' : event
    }

    if event_images.exists() : 
        context['images'] = '@'.join([i.image.url for i in event_images])

    if request.method == 'POST' : 
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']

        visitor = Visitor.objects.create(
            full_name = full_name,
            email = email,
            phone = phone,
            event = event
        )

        if 'img' in request.FILES :
            img = request.FILES['img']
            visitor.picture = img
        
        visitor.save()

        context['msg'] = 'تم تسجيلك بنجاح'

        return redirect('visitor_register',eventuuid)

    return render(request,'visitor-register.html',context)