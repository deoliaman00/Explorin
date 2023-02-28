from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import TodoSerializers
from .models import Todo

class TodoView(viewsets.ModelViewSet):
    serializer_class=TodoSerializers
    queryset=Todo.objects.all()