from django import forms

from webapp.models import Photos


class PhotosForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = ('image', 'signature')
