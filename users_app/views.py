from django.shortcuts import render, HttpResponse



def login (request) :
    return HttpResponse('Login Page')


def register(request) : 
    return HttpResponse('Regsiter page')


