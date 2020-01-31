from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import forms
from . import models


def sign_in(request):
    pass


def register(request):
    """Create new user account"""
    form = forms.UserRegisterForm()
    if request.method == 'POST':
        form = forms.UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username = form.cleaned_data['username'],
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password1'],
            )
            login(request, user)
            messages.success(
                request,
                "You have successfully created a new acount and are " +
                f"now logged in as {user.username}"
            )
            return HttpResponseRedirect(reverse('index'))
    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )


def logout(request):
    pass
