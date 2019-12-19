from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length = 50)
    caption = HTMLField()
    comments = models.TextField()
    

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'images/')
    bio =  models.TextField()


