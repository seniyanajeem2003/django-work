from django import forms
from .models import home15
class Teacher_Form(forms.ModelForm):
    class Meta:
        model = home15
        fields = '__all__'