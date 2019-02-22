from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators
from django.utils.translation import gettext_lazy as _

from . import models


def must_be_empty(value):
    if value:
        raise forms.ValidationError('Is not empty')


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=_("Your password can't be too similar to your other " +
        "personal information, must contain at least 8 characters, can't be " +
        "a commonly used password, and can't be completely numeric.")
    )
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)
        help_texts = {
            'username': "Your username can contain letters, " +
            "digits and the @/./+/-/_ characters only."
        }
