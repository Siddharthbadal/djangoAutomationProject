from django import forms
from .models import CompressImage

class ImageCompressionForm(forms.ModelForm):
    class Meta:
        model = CompressImage
        fields = ['original_image','quality']

    original_image = forms.ImageField(label='Uplaod your Image')
    