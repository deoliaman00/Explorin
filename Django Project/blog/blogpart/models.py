from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# this is where we write our database and futher this is 
# used in the data tables 
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    dateposted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(null=True,blank=True,upload_to='article_pics')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    