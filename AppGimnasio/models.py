from cgitb import text
from django.db import models


# Create your models here.

class registro(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    edad = models.IntegerField()
    email= models.EmailField()
    dni = models.IntegerField()
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre,self.dni)

class actividades(models.Model):
    tipo= models.CharField(max_length=30)

class horarios(models.Model):
    tipo= models.CharField(max_length=30)
    hora_entrada = models.ImageField(max_length=2)
    hora_salida = models.ImageField(max_length=2)

class contacto(models.Model):
    nombre= models.CharField(max_length=30)
    email= models.EmailField()
