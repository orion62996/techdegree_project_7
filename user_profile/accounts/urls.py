"""user_profile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views.static import serve

from . import views

app_name = 'accounts'
urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),  # Used to upload image files, other files can also be uploaded word, ppt, etc.
    path('static/<path:path>', serve, {'document_root': settings.STATIC_ROOT}),
    path('change-password/', views.change_password, name='change_password'),
    path('edit', views.edit_profile, name='edit'),
    path('login', views.sign_in, name='login'),
    path('logout', views.sign_out, name='logout'),
    path('profile', views.profile, name='profile'),
    path('register', views.register, name='register'),
    path('select-avatar', views.select_avatar, name='select_avatar'),
    path('crop-avatar', views.crop_avatar, name="crop_avatar"),
]
urlpatterns += staticfiles_urlpatterns()
