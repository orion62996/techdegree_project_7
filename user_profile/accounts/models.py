from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from tinymce.models import HTMLField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='avatar_pics')
    dob = models.DateField(null=True, blank=True)
    bio = HTMLField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    ice_cream_flavor = models.CharField(max_length=255, blank=True)


    # def save(self, *args, **kwargs):
    #     super().save()
    #
    #     img = Image.open(self.avatar.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.avatar.path)
