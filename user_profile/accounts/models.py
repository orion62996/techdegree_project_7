from django.contrib.auth.models import User
from django.db import models

from avatar_editor.models import Avatar


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    hobby = models.CharField(max_length=255, blank=True)
    avatar = models.ForeignKey(Avatar, on_delete=models.CASCADE)
