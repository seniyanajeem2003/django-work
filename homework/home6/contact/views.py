from django.shortcuts import render
from .forms import ContactForm
from .models import contact_data

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cust = contact_data()
            cust.fname = form.cleaned_data['fname']
            cust.email = form.cleaned_data['email']
            cust.pnumber = form.cleaned_data['pnumber']
            cust.save()
            return render(request, 'forms-data.html', {
                'fname':cust.fname,
                'email': cust.email,
                'pnumber': cust.pnumber,
                'message': 'Data saved to DB'
            })
    else:
        form = ContactForm()
    return render(request, 'page1.html', {'form': form})


