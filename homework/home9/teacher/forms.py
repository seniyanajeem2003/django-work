from django import forms
from .models import teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ['name', 'subject']

