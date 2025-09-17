from django.db import models

class class6(models.Model):
    name= models.CharField(max_length=50)
    year = models.CharField(max_length=100)

