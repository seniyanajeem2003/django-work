from django.db import models
from django.core.validators import validate_email
class home7(models.Model):
    name= models.CharField(max_length=50)
    email = models.CharField(max_length=100,validators=[validate_email])
   