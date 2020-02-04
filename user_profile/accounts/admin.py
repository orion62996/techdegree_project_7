from django.contrib import admin
from image_cropping import ImageCroppingMixin

from .models import UserProfile

class UserProfileAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(UserProfile, UserProfileAdmin)
