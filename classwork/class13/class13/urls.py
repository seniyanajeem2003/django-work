"""
URL configuration for class13 project.

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

from django.urls import path
from shop import views

urlpatterns = [
   path('createproduct', views.create_product, name='createproductapi'),
   path('listproducts', views.list_products, name='retrieveproductapi'),
   path('<int:pk>/updateproduct', views.update_product, name='updateproductapi'),
   path('<int:pk>/deleteproduct', views.delete_product, name='deleteproductapi'),
]
