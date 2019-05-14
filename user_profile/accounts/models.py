from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from tinymce.models import HTMLField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    bio = HTMLField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    ice_cream_flavor = models.CharField(max_length=255, blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()


class Photo(models.Model):
    file = models.ImageField()
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'
