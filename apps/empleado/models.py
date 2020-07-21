from django.db import models
from apps.departamento.models import Departamen
class Empleado(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=20)
    fechanac= models.DateField()
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=20)
    fechaingreso=models.DateField()
    puesto = models.CharField(max_length=50)
    salario = models.IntegerField()
    departamento=models.ForeignKey(Departamen, null=True,blank=True,on_delete=models.CASCADE)