from django import forms
class ContactForm(forms.Form):
    fname = forms.CharField(max_length=100,min_length=5)
    email = forms.CharField(max_length=100,min_length=10)
    pnumber = forms.CharField(max_length=50,min_length=10)