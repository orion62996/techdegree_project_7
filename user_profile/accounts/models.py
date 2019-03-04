from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    avatar = models.ImageField(default='default.jpg', upload_to='avatar_pics')
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    ice_cream_flavor = models.CharField(max_length=255, blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)
