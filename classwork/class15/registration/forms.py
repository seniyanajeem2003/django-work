from django import forms
from .models import class15
class Student_Form(forms.ModelForm):
    class Meta:
        model = class15
        fields = '__all__'