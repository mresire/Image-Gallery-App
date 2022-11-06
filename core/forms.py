from django import forms
from .models import Photo 


# Create your forms here.
class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        exclude = ['owner']