from django import forms
from .models import Record


class ImageForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = 'image'
