from email.policy import default
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Album(models.Model):
    album_name = models.CharField(max_length=150)
    created_at = models.DateField(default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Photos(models.Model):
    photoname = models.CharField(max_length=100, default=None)
    photo = models.ImageField( upload_to = 'photo/' ,default = None)
    posted_at = models.DateField(default = datetime.now)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, default = None)