from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre_apellido = models.CharField(verbose_name='Nombre y Apellido', max_length=200)
    direccion = models.CharField(verbose_name='Direccion', max_length=200)
    pais = models.CharField(verbose_name='Pais')
    ciudad = models.CharField(verbose_name='Ciudad')