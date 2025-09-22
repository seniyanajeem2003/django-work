from django import forms
from .models import home10

class SchoolForm(forms.ModelForm):
    class Meta:
        model = home10
        fields = ['name','course','age']