from django import forms
from django.core import validators


def must_be_empty(value):
    if value:
        raise forms.ValidationError('Is not empty')


class SignUpForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    varify_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        verify = cleaned_data.get('verify_password')

        if password != verify:
            raise forms.ValidationError("You did not enter the same password in both fields")
