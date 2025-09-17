from django import forms
from .models import home7
class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = home7
        fields = ['name','email']