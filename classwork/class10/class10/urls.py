"""
URL configuration for class10 project.

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
from library import views
from django.urls import path

urlpatterns = [
        path('create/',views.library_create,name='createlibrary'),
        path('',views.library_read,name='home'),
        path('update/<int:id>/',views.library_update,name='updatelibrary'),
        path('delete/<int:id>/', views.library_delete, name='deletelibrary'),
    
    ]
