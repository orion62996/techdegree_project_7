from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.core import validators
from django.core.files import File
from django.utils.translation import gettext, gettext_lazy as _
from PIL import Image

from . import models
from . import validators as custom_validators


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text="""
        <ul>
            <li>Your password can't be too similar to your other personal information.</li>
            <li>Your password can't be a commonly used password.</li>
            <li>Your password can't be entirely numeric.</li>
            <li>Your password must contain at least 14 characters.</li>
            <li>Your password must contain uppercase and lowercase letters.</li>
            <li>Your password must contain at least one numeric digit.</li>
            <li>Your password must contain at least one special character.</li>
        </ul>
        """
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
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
            validators.MinLengthValidator(
                limit_value=10,
                message=_("Make sure your bio has at least 10 characters.")
            )
        )

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
            'ice_cream_flavor',
        )


class PhotoForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = models.Photo
        fields = (
            'file',
            'x',
            'y',
            'width',
            'height',
        )

    def save(self):
        photo = super(PhotoForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(photo.file)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
        resized_image.save(photo.file.path)

        return photo
