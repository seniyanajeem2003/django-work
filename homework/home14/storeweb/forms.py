from django import forms
from .models import home14
class ProductModelForm(forms.ModelForm):
    class Meta:
        model = home14
        fields = '__all__'