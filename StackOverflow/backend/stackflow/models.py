from django.db import models

## this is for handling the user details for now
class User(models.Model):
    username=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=255)

## this will make sure of all the things while creating a 
class Question(models.Model):
    GENRE_CHOICES = [
        ('NS','NODEJS'),
        ('DJ','Django'),
        ('FB','Facebook'),
        ('HU','Heroku'),
        ('IS','ISRO'),
    ]
    title = models.CharField(max_length=255)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)
    num_answers = models.PositiveIntegerField(default=0)
    num_comments = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=255, choices=GENRE_CHOICES)
    
    def __str__(self):
        return self.title
    def get_tags_display(self):
        return [choice[1] for choice in self.GENRE_CHOICES if choice[0] in self.tags]


class Answer(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # add other fields as needed

