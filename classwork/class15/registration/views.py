from django.shortcuts import render
from .forms import Student_Form
from .models import class15
from django.http import HttpResponse

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
def student_profile(request):
    form = Student_Form()
    if request.method == 'POST':
        form = Student_Form(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.id_card = request.FILES['id_card']
            file_type = student.id_card.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                return HttpResponse('file type you uploaded is not supported')
            student.save()
            return HttpResponse('file uploaded successfully')
    context = {"form": form,}
    return render(request, 'studentupload.html', context)