from django.shortcuts import render, redirect
from .models import teacher
from .forms import TeacherForm

def teacher_list(request):
    teachers = teacher.objects.all()
    return render(request, 'teachers/teachers_list.html', {
        "teachers": teachers,
        "message": "Welcome to the Teachers Page!"
    })

def teacher_form(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teachers:teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'teachers/teachers_form.html', {"form": form})
