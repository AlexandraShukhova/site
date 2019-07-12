
from django.db import models

class Cat(models.Model):
    name = models.CharField(max_length=64)
    #foto = models.ImageField(null=True, blank=True, upload_to='images/')
    age = models.CharField(max_length=64)
    gender = models.CharField(max_length=64)
    vetpasport = models.CharField(max_length=64)
    lotok = models.CharField(max_length=64)

    def __str__(self):
        return 'Cat: {}'.format(self.name, self.gender)