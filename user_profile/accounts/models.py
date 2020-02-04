from django.contrib.auth.models import User
from django.db import models
from image_cropping import ImageCropField, ImageRatioField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = ImageCropField(default='images/default.jpeg', upload_to='images')
    dob = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    hobby = models.CharField(max_length=255, blank=True)
    cropping = ImageRatioField('avatar', '300x300')
