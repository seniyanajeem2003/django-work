"""
URL configuration for home14 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from storeweb import views
from django.urls import path

urlpatterns = [
        path('',views.product_create,name='home'),
        path('list/',views.product_read,name='list'),
        path('<int:pk>/pdf/', views.generate_pdf, name='pdf'),
        path('product_email/<int:pk>/', views.send_product_email, name='email'),
    ]