
from django.shortcuts import render, redirect
from .forms import LibraryForm
def library_create(request):
    if request.method == 'POST':
        form = LibraryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =LibraryForm()
    return render(request, 'create.html', {'form': form})

def library_read(request):
    library_list=class10.objects.all()
    return render(request,'home.html',{'library_list':library_list})

def library_update(request, id):
    library = class10.objects.get(pk=id)
    if request.method == 'POST':
        form = LibraryForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =LibraryForm(instance=library)           
    return render(request, 'update.html', {'form': form})