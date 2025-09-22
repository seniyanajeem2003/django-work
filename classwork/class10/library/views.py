
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LibraryForm
from .models import class10
from django.core.paginator import Paginator

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
    library_list = class10.objects.all().order_by('id')
    paginator = Paginator(library_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj})

def library_update(request, id):
    library = get_object_or_404(class10, pk=id)
    if request.method == 'POST':
        form = LibraryForm(request.POST,instance=library)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =LibraryForm(instance=library)           
    return render(request, 'update.html', {'form': form})

def library_delete(request, id):
    book_delete = get_object_or_404(class10, pk=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('home')
    return render(request, 'delete.html', {'book_delete': book_delete})

