from django.db import models

class home15(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length = 200)
    subject = models.CharField(max_length=500)
    years_of_experience = models.CharField(max_length=200)
    photo = models.FileField()
    def __str__(self):
        return self.firstname
