from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField()
    email = models.EmailField(max_length=255)
    avatar = models.FilePathField()
    bio = models.TextField()
    location = models.CharField(max_length=255)
    ice_cream_flavor = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now=True)
