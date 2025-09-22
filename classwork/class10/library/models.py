from django.db import models

class class10(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=60)
    year = models.CharField(max_length=10)