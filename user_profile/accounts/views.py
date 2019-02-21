from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from . import forms


def register(request):
    """Display the registration form."""
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 "You have been successfully registered!")
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'register.html', {'form': form})


def login(request):
    """Display the login form."""
    return render(request, 'login.html')


def logout(request):
    """Log the user out."""
    pass


def profile(request):
    """Display the user's profile."""
    return render(request, 'profile.html')


def edit_profile(request):
    """Allow the user to edit their profile."""
    return render(request, 'edit_profile.html')


def change_password(request):
    """Display password change form."""
    return render(request, 'change_password.html')
