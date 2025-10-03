from django.shortcuts import render
from .forms import Teacher_Form
from .models import home15
from django.http import HttpResponse

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
def teacher_profile(request):
    form = Teacher_Form()
    if request.method == 'POST':
        form = Teacher_Form(request.POST, request.FILES)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.photo = request.FILES['photo']
            file_type = teacher.photo.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                return HttpResponse('file type you uploaded is not supported')
            teacher.save()
            return HttpResponse('file uploaded successfully')
    context = {"form": form,}
    return render(request, 'teacherprofile.html', context)