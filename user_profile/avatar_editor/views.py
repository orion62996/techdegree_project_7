from django.shortcuts import get_object_or_404, render

from . import models


def edit_avatar(request, pk):
    avatar = get_object_or_404(models.Avatar, pk=pk)
    return render(request,
                  'avatar_editor/edit_avatar.html',
                  {'avatar': avatar})
