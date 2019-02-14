from django import forms
from django.core import validators


def must_be_empty(value):
    if value:
        raise forms.ValidationError('Is not empty')


class RegisteredUserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    validate_password = forms.CharField()
    honeypot = forms.CharField(required=False,
                               widget=forms.HiddenInput,
                               label="Leave this blank",
                               validators=[must_be_empty])

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('password')
        varify = cleaned_data.get('validate_password')
        if email != varify:
            raise forms.ValidationError("The passwords do not match")


class UserProfileForm(forms.Form):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    birthday = forms.DateField()
    email = forms.EmailField()
    bio = forms.CharField(widget=forms.Textarea)
    location = forms.CharField()
    ice_cream_flavor = forms.CharField()
    honeypot = forms.CharField(required=False,
                               widget=forms.HiddenInput,
                               label="Leave this blank",
                               validators=[must_be_empty])
