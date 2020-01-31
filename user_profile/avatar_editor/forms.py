from django import forms
from django.core.files import File

from PIL import Image

from . import models


class AvatarEditForm(forms.ModelForm):
    x = forms.FloatField()
    y = forms.FloatField()
    width = forms.FloatField()
    height = forms.FloatField()

    class Meta:
        model = models.Avatar
        fields = [
            'x',
            'y',
            'width',
            'height',
        ]

    def save(self):
        avatar = super(AvatarEditForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        photo = models.Avatar.objects.get(pk=1)
        image = Image.open(photo.file)
        cropped_image = image.crop((x, y, w+x, h+y))
        cropped_image.save(photo.file.path)

        return avatar
