from django.shortcuts import render, HttpResponse, redirect
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


