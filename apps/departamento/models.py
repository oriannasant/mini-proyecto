from django.db import models

# Create your models here.
class Departamen(models.Model):
    nombre = models.CharField(max_length=50)
    localizacion = models.CharField(max_length=256)