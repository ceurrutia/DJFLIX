from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre_apellido = models.CharField(verbose_name='Nombre y Apellido', max_length=500)
    direccion = models.CharField(verbose_name='Direccion', max_length=700)
    dni = models.TextField(verbose_name= "DNI", max_length=350)
    email = models.CharField(verbose_name="Email", max_length=250)
    pais = models.CharField(verbose_name='Pais', max_length=200)
    ciudad = models.CharField(verbose_name='Ciudad', max_length=200)

    def __str__(self) -> str:
        return f'{self.nombre_apellido} - {self.dni}'
