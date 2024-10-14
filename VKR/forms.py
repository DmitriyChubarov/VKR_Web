from django import forms

class ImageUploadForm(forms.Form):
    size = forms.IntegerField(min_value=2, max_value=9)
    image = forms.ImageField(label='')