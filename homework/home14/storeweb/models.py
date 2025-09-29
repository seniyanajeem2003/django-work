from django.db import models

class home14(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=50)
    price= models.FloatField()