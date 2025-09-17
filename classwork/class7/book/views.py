from django.shortcuts import render


from .forms import BooksModelForm
from .models import class7
def page1(request):
    if request.method == 'POST':
        form = BooksModelForm(request.POST)
        if form.is_valid():
            form.save()
            books= class7.objects.all()
            return render(request,'forms-data.html',{
                 'books': books})
    else:
        form = BooksModelForm()
    return render(request,'page1.html',{'form':form})
