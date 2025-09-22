from django.shortcuts import render, redirect, get_object_or_404
from .models import home10
from .forms import SchoolForm

def school_create(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =SchoolForm()
    return render(request, 'create.html', {'form': form})

def school_read(request):
    
    student_list = home10.objects.all()
    return render(request, 'home.html', {'student_list': student_list})


def school_update(request, id):
    student_update = get_object_or_404(home10, pk=id)
    if request.method == 'POST':
        form = SchoolForm(request.POST,instance=student_update)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =SchoolForm(instance=student_update)           
    return render(request, 'update.html', {'form': form,'student_update':student_update})
 

def school_delete(request,id):
    student_delete= get_object_or_404(home10, pk=id)
    if request.method == 'POST':
        student_delete.delete()
        return redirect('home')
    
    return render(request,'delete.html',{'student_delete':student_delete})