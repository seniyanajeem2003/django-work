from django.shortcuts import render, redirect
from .forms import ProductModelForm
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from .models import home14
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

def product_create(request):
    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =ProductModelForm()
    return render(request, 'home.html', {'form': form})


def product_read(request):
    product_list=home14.objects.all()
    return render(request,'list.html',{'product_list':product_list})



def generate_pdf(request,pk):
    product = get_object_or_404(home14,pk=pk)
    template = get_template('product_pdf.html')
    html = template.render({'product': product})
   
    buffer = BytesIO()

    pisa_status = pisa.CreatePDF(html, dest=buffer)

    if pisa_status.err:
        return HttpResponse('PDF creation error!')
    else:
        response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(product.name)
        return response
    

def send_product_email(request,pk):
    product=home14.objects.get(pk=pk)

    subject = f"New Product: {product.name}"
    from_email = "user123@gmail.com"
    recipient_list = ["your_mailtrap_inbox@mailtrap.io"]
    html_message = render_to_string('product_email.html', {'product': product})
    plain_message = strip_tags(html_message)
    send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)
    return HttpResponse('Email sent successfully')