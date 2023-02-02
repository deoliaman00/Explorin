from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blogpart/home.html',context)


def about(request):
    return render(request,'blogpart/about.html',{'title':'Aman About Page'})