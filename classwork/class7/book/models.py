
from django.db import models

class class7(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)