from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _

from bootstrap_datepicker_plus import DatePickerInput
from image_cropping import ImageCropWidget

from . import models


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
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
            'password1',
            'password2',
        ]


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
    class Meta:
        model = models.UserProfile
        fields = (
            'avatar',
        )
