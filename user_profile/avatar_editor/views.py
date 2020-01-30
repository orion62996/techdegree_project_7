from django.shortcuts import render


def edit_avatar(request):
    return render(request, 'avatar_editor/edit_avatar.html')
