from django.contrib.auth.models import User
from django.db import models

from django_summernote.fields import SummernoteTextField


class UserProfile(models.Model):
    """A user profile model that extends the built-in user model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='images/default.jpeg', upload_to='images')
    dob = models.DateField(null=True, blank=True)
    bio = SummernoteTextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    hobby = models.CharField(max_length=255, blank=True)
