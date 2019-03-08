from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.core import validators

from . import models


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
        )


class UserProfileUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserProfileUpdateForm, self).__init__(*args, **kwargs)
        bio_field = self.fields['bio']
        bio_field.validators.append(
            validators.MinLengthValidator(limit_value=10)
        )

    class Meta:
        model = models.UserProfile
        fields = (
            'dob',
            'bio',
            'location',
            'ice_cream_flavor',
        )


class UserAvatarForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = (
            'avatar',
        )
