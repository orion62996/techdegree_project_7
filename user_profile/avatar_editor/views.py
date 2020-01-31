from django.shortcuts import get_object_or_404, redirect, render

from . import forms
from . import models


def edit_avatar(request, pk):
    avatar = get_object_or_404(models.Avatar, pk=pk)
    form = forms.AvatarEditForm()
    if request.method == 'POST':
        form = forms.AvatarEditForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,
                  'avatar_editor/edit_avatar.html',
                  {'avatar': avatar, 'form': form})
