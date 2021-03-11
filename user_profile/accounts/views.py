from django.contrib import messages
from django.contrib.auth import (authenticate, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from . import forms
from . import models


def sign_in(request):
    """Process the user login request"""
    form = AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            if form.user_cache is not None:
                user = form.user_cache
                if user.is_active:
                    login(request, user)
                    messages.success(
                        request,
                        f"You are now logged in as {user.username}"
                    )
                    return HttpResponseRedirect(reverse('index'))
                else:
                    messages.error(
                        request,
                        "That user account has been disabled"
                    )
            else:
                message.error(
                    request,
                    "The username or password is incorrect"
                )
    return render(
        request,
        'accounts/login.html',
        {'form': form, 'login_page': 'active'}
    )


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
        {'form': form, 'registration_page': 'active'}
    )


def sign_out(request):
    """Log the user out of the site"""
    logout(request)
    messages.success(request, "You've been logged out. Come back soon!")
    return HttpResponseRedirect(reverse('index'))


@login_required
def profile(request):
    """Display the details of the user's profile"""
    user = request.user
    user_profile = get_object_or_404(models.UserProfile, user_id=user.id)
    return render(
        request,
        'accounts/profile.html',
        {'user': user, 'user_profile': user_profile, 'profile_page': 'active'}
    )


@login_required
def edit_profile(request):
    """Edit the details of the user's profile"""
    if request.method == 'POST':
        user_update_form = forms.UserUpdateForm(
            request.POST,
            instance=request.user
        )
        user_profile_update_form = forms.UserProfileUpdateForm(
            request.POST,
            instance=request.user.userprofile
        )
        user_avatar_form = forms.UserAvatarForm(
            request.POST,
            request.FILES,
            instance=request.user.userprofile
        )
        if user_update_form.is_valid() and user_profile_update_form.is_valid():
            user_update_form.save()
            user_profile_update_form.save()
            user_avatar_form.save()
            messages.success(request, "Your profile has been updated!")
            return HttpResponseRedirect(reverse('accounts:profile'))
    else:
        user_update_form = forms.UserUpdateForm(
            instance=request.user
        )
        user_profile_update_form = forms.UserProfileUpdateForm(
            instance=request.user.userprofile
        )
        user_avatar_form = forms.UserAvatarForm(
            instance=request.user.userprofile
        )
    return render(request,
                  'accounts/edit_profile.html',
                  {
        'user_update_form': user_update_form,
        'user_profile_update_form': user_profile_update_form,
        'user_avatar_form': user_avatar_form,
        'edit_profile_page': 'active'
    })


@login_required
def change_password(request):
    """Allow the user to change their password"""
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request,
                "Your password was successfully updated"
            )
            return HttpResponseRedirect(reverse('accounts:profile'))
        else:
            messages.error(request, "Please correct the error below")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})


@login_required
def edit_avatar(request):
    """Testing cropperjs"""
    user = request.user
    user_profile = get_object_or_404(models.UserProfile, user_id=user.id)
    return render(
        request,
        'accounts/edit_avatar.html',
        {'user': user, 'user_profile': user_profile}
    )
