from django import forms
from .models import class7
class BooksModelForm(forms.ModelForm):
    class Meta:
        model = class7
        fields = ['title','author']
