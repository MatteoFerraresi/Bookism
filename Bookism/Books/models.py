from email.quoprimime import body_check
from multiprocessing import AuthenticationError
from turtle import title
from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    #author

    def __str__(self):
        return self.title #to show title in database shell


    def snippet(self):
        return self.body[:50] + '...'



