from django.db import models

class class15(models.Model):
    fname = models.CharField(max_length=200)
    course = models.CharField(max_length = 200)
    pnumb = models.CharField(max_length=500)
    email = models.EmailField(default = None)
    id_card = models.FileField()
    def __str__(self):
        return self.fname