from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Feature
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def index(request):
    features=Feature.objects.all()
    return render(request,'index.html',{'features':features}) 

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already Exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password Not the Same')
            return redirect('register')
        
    return render(request,'register.html')

def countW(request):
    text=request.POST['text']
    amt_of_words=len(text.split())
    return render(request,'count.html',{'amt_of_words':amt_of_words})

def login(request):
    return render(request,'login.html')