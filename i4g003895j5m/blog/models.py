from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    title = models.TextField()
    Author = models.get_user_model()
    created_date = models.DateTimeField('Created published')
    Published_date= models.DateTimeField('date published')
