from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length = 50)
    caption = HTMLField()
    comments = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering =['title']

    def save_caption(self):
        self.save()

    def delete_caption(self):
        self.delete()

    @classmethod
    def get_captions(cls):
        captions = cls.objects.all()

        return captions
    

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'images/')
    bio =  models.TextField()
    location = models.CharField(max_length=100)


