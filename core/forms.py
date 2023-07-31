from django import forms
from .models import imageData

class ImageForm(forms.ModelForm):
    class Meta:
        model = imageData
        fields = ["image"]