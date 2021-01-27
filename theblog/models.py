from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from . import news_extractor


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="News & Blogs")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + "  |  " + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')

class News(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(max_length=300)
    urls = models.URLField(max_length = 200)

    def __str__(self):
        return self.title + "  |  " + str(self.author)

    


    


