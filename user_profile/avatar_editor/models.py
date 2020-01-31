from django.db import models


class Avatar(models.Model):
    file = models.ImageField(upload_to='images')
    uploaded_at = models.DateTimeField(auto_now_add=True)


# class EditedAvatar(models.Model):
#     file = models.ImageField(upload_to='images')
#     uploaded_at = models.DateTimeField(auto_now_add=True)
#     avatar = models.ForeignKeyField()
