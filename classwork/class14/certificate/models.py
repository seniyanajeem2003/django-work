from django.db import models
class class14(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=50)
    date= models.DateField()