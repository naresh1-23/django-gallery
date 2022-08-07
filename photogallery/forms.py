from .models import Album, Photos
from django import forms
class albumform(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album_name']




