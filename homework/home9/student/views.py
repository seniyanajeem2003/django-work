from django.shortcuts import render, redirect
from .models import student
from .forms import StudentForm

def student_list(request):
    students = student.objects.all()
    return render(request, 'students/students_list.html', {
        "students": students,
        "message": "Welcome to the Students Page!"
    })

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:student_list')
    else:
        form = StudentForm()
    return render(request, 'students/students_form.html', {"form": form})
