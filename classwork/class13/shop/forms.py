from django import forms
from .models import class13

class ProductForm(forms.ModelForm):
    class Meta:
        model = class13
        fields = ['name','price']