from django.shortcuts import render
from django.http import HttpResponse
from .models import Credential
import json


global a
a = {'usernames':[],'passwords':[],'emailids':[]}

def index(request):
    return render(request,'index.html')

def gotologin(request):
    return render(request,'loginPage.html')

def gotoregister(request):
    return render(request,'register.html') 

def register(request):
    Username = request.GET.get('username')
    Password = request.GET.get('password')
    Email = request.GET.get('emailid')
    FirstName = request.GET.get('first name')
    LastName = request.GET.get('last name')

    if(len(list(Credential.objects.all().filter(email_id=Email).values())))==0:
        Credential(email_id=Email,password=Password,firstName=FirstName,lastName=LastName).save()
    else:   
        return HttpResponse("You already have an account. Please <a href='/loginpage'> Login </a>")
    
    return render(request,'loginpage.html')

def login(request):
    Email = request.GET.get('emailid')
    Password = request.GET.get('password')

    if(len(list(Credential.objects.all().filter(email_id=Email).values())))==1:
        if(Credential.objects.all().filter(email_id=Email).values()[0]['password'] == Password):
            return render(request,'home.html')
        else:
            return HttpResponse("Password Wrong <br> Please retry <a href='/loginpage'> Login </a>")
    else:
        return HttpResponse("Please retry <a href='/loginpage'> Login </a> OR <a href='/registerpage'> Register </a>")
