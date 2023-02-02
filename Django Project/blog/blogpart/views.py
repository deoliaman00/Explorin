from django.shortcuts import render
from django.http import HttpResponse


posts=[
    {
        'title':'Aman Deoli',
        'tag': 'Military',
        'words':'50'
    },
    {
        'title':'Naman Defu',
        'tag': 'Airforce',
        'words':'52'
    }
]

def home(request):
    context={
        'posts':posts
    }
    return render(request,'blogpart/home.html',context)


def about(request):
    return render(request,'blogpart/about.html',{'title':'Aman About Page'})