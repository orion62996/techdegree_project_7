from django import forms
from django.contrib.auth.models import User
from django.core import validators

from . import models


def must_be_empty(value):
    if value:
        raise forms.ValidationError('Is not empty')


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
