from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# this is where we write our database and futher this is 
# used in the data tables 
class Tags(models.Model):
    category=models.CharField(max_length=100)
    def __str__(self):
        return self.category


class SoftDeleteManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)
        
class SoftDeleteModel(models.Model):

    deleted_at = models.DateTimeField(null=True, default=None)
    objects = SoftDeleteManager()
    all_objects = models.Manager()

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True

class Post(SoftDeleteModel):
    title=models.CharField(max_length=100)
    content=models.TextField()
    dateposted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(null=True,blank=True,upload_to='article_pics')
    tags=models.ManyToManyField(Tags)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})



