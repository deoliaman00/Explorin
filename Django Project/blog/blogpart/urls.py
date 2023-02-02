from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='blogpart-home'),
    path('about/', views.about, name='blogpart-about'),
]
