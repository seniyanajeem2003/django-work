from django.db import models

class home10(models.Model):
    name = models.CharField(max_length=500)
    course = models.CharField(max_length=50)
    age = models.CharField(max_length=10)