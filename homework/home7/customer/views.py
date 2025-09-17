from django.shortcuts import render
from .forms import CustomerModelForm
from .models import home7
def page1(request):
    if request.method == 'POST':
        form = CustomerModelForm(request.POST)
        if form.is_valid():
            form.save()
            form= CustomerModelForm()
    else:
        form = CustomerModelForm()
    return render(request,'page1.html',{'form':form})

def page2(request):
    customers = home7.objects.all().order_by('name')  
    return render(request, 'page2.html', {'customers': customers})

def page3(request):
    customers = home7.objects.filter(email__endswith='@example.com').order_by('name')
    return render(request, 'page3.html', {'customers': customers})