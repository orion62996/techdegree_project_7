from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from .models import UserProfile

class UserProfileAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(UserProfile, UserProfileAdmin)
