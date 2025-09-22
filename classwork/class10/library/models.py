from django.db import models

class class10(models.Model):
    title = models.CharField(max_length=500)
    author = models.TextField()
    year = models.CharField(max_digits=10)