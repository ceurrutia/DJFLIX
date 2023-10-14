from django.db import models

# Create your models here.
class Pelicula(models.Model):
    nombre = models.CharField(verbose_name="Nombre pelicula", max_length= 250)
    anio_estreno = models.DateField(verbose_name="Año de estreno")
    categoria = models.CharField(verbose_name="Categoria", max_length=100)
    imagen = models.CharField(verbose_name="imagen", max_length=500)
    descripcion = models.CharField(verbose_name="Descripción: ", max_length= 800)
    duracion = models.CharField(verbose_name="Duración", max_length=100)
    es_serie = False
    
def __str__(self) -> str:
        return f'{self.nombre}, {self.anio_estreno}, {self.categoria}, {self.imagen}, {self.descripcion}, {self.duracion} '
    


class Serie(Pelicula):
        cant_capitulos = models.IntegerField(verbose_name="Cantidad de capitulos")
        nombre_capitulo = models.TextField(verbose_name= "Nombre capitulo", max_length= 200)
        
        
def __str__(self) -> str:
        return f'{self.cant_capitulos}, {self.nombre_capitulo}'
