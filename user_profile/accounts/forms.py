from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files import File
from django.utils.translation import gettext, gettext_lazy as _

from bootstrap_datepicker_plus import DatePickerInput
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteInplaceWidget

from . import models


def must_match_field(value):
    pass


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Please verify your email address")
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text="""
        <ul>
            <li>Your password can't be too similar to your other personal information</li>
            <li>Your password can't be a commonly used password</li>
            <li>Your password can't be entirly numeric</li>
            <li>Your password must contain at least 14 characters</li>
            <li>Your password must contain uppercase and lowercase letters</li>
            <li>Your password must contain at least one numeric digit</li>
            <li>Your password must contain at least one special character</li>
        </ul>
        """
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'verify_email',
            'password1',
            'password2',
        ]

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        verify = cleaned_data.get('verify_email')

        if email != verify:
            raise forms.ValidationError(
                "You need to enter the same email address in both fields"
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
    dob = forms.DateField(
        widget = DatePickerInput(format='%m/%d/%Y'),
        label = _("Date of Birth"),
        required = False,
    )

    class Meta:
        model = models.UserProfile
        fields = (
            'dob',
            'bio',
            'location',
            'hobby',
        )


class UserAvatarForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = models.UserProfile
        fields = ('avatar',)


class CropAvatarForm(forms.Form):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())
    rotate = forms.IntegerField(widget=forms.HiddenInput())
    flip = forms.IntegerField(widget=forms.HiddenInput())
