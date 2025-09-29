from django import forms
from .models import class14
class StudentModelForm(forms.ModelForm):
    class Meta:
        model = class14
        fields = ['name', 'course','date']