from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.teacher_list, name='teacher_list'),
    path('form/', views.teacher_form, name='teacher_form'),
]
