from django.db import models

class teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

   