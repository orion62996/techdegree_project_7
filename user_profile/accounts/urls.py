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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('change-password/', views.change_password, name='change_password'),
    path('edit', views.edit_profile, name='edit'),
    path('edit-avatar', views.edit_avatar, name='edit_avatar'),
    path('login', views.sign_in, name='login'),
    path('logout', views.sign_out, name='logout'),
    path('profile', views.profile, name='profile'),
    path('register', views.register, name='register'),
]
urlpatterns += staticfiles_urlpatterns()
