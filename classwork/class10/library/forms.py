from django import forms
from .models import class10

class LibraryForm(forms.ModelForm):
    class Meta:
        model = class10
        fields = ['title', 'author', 'year']