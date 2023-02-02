from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# this is where we write our database and futher this is 
# used in the data tables 
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    dateposted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    

