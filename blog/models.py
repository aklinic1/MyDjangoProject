from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model): #each class is its own table in db
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # with CASCADE we tell our model that if user is deleted posts are also but not the other way around

    def __str__(self):
        return self.title6

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

#reverse function returns a full url to a route as a string a let the class view handle the redirect
#redirect function redirects to a specific route



# Create your models here.
