from django.db import models

# Create your models here.

class Portafolio(models.Model):

    cliente = models.CharField(max_length=40)
    agencia = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.cliente} - {self.agencia}'

class Quienes_Somos(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    mensaje = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.mensaje}'

class Servicios(models.Model):

    tipo = models.CharField(max_length=40)
    costo = models.IntegerField()
    descripcion = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.tipo} {self.costo} {self.descripcion}'
