from django.db import models

class home13(models.Model):
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=50)
    title= models.CharField(max_length=50,default="Untitled")
    message = models.TextField(blank=True)