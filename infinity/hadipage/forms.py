from django import forms
from .models import *

class AddPostForm(forms.ModelForm):
    class Meta:
        model= zavedeniya
        fields='__all__'
