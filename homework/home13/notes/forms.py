from django import forms
from .models import home13

class NotesForm(forms.ModelForm):
    class Meta:
        model = home13
        fields = '__all__'