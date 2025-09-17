from django import forms
from .models import class6
class MoviesModelForm(forms.ModelForm):
    class Meta:
        model = class6
        fields = ['name','year']
