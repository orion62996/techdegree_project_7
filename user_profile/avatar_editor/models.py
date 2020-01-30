from django.db import models


class Avatar(models.Model):
    file = models.ImageField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
