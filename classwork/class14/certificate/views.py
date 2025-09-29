from django.shortcuts import render, redirect
from .forms import StudentModelForm
from .models import class14 
from django.shortcuts import get_object_or_404, render
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from .models import class14
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

def student_create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =StudentModelForm()
    return render(request, 'home.html', {'form': form})

def student_read(request):
    student_list=class14.objects.all()
    return render(request,'list.html',{'student_list':student_list})



def generate_pdf(request, pk):
    student = get_object_or_404(class14, pk=pk)
    template = get_template('student_pdf.html')
    html = template.render({'student': student}, request)

    buffer = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=buffer)

    if pisa_status.err:
        return HttpResponse("PDF creation error!", content_type="text/plain")

    response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(student.name)
    return response


def send_student_email(request,pk):
    student=class14.objects.get(pk=pk)

    subject = f"Student Name: {student.name}"
    from_email = "user123@gmail.com"
    recipient_list = ["your_mailtrap_inbox@mailtrap.io"]
    html_message = render_to_string('student_email.html', {'student': student})
    plain_message = strip_tags(html_message)
    send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)
    return HttpResponse('Email sent successfully')