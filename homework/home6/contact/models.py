from django.db import models
class contact_data(models.Model):
    fname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    pnumber = models.CharField(max_length=50)

