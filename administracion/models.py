from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Persona(models.Model):
    nombre_apellido = models.CharField(verbose_name='Nombre y Apellido', max_length=500)
    dni = models.IntegerField(verbose_name= "DNI")
    email = models.EmailField(verbose_name="Email", max_length=250)

    def __str__(self) -> str:
        return f'{self.nombre_apellido} - {self.dni} -  {self.email} '


    def clean_dni(self):
        #len(str(self.cleaned_data['dni'])) == 8
        if (0 < self.cleaned_data['dni'] <= 99999999):
            raise ValidationError("El dni es un número positivo y no tiene más de 8 dígitos")
        
        return self.cleaned_data['dni']

    def clean_email(self):
        if self.cleaned_data['email'] == 'email':
            raise ValidationError("El mail que está usando ya está siendo usado")
        
        return self.cleaned_data['email']


    class Meta:
     abstract = True
     
    
        
class Suscriptor(Persona):
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")
    baja = models.DateField(verbose_name="baja", default=False)


class Categorias(models.Model):
    nombre_categoria = models.CharField(verbose_name="Nombre categoria", max_length=100)


class Pelicula(models.Model):
    nombre_pelicula = models.CharField(verbose_name="Nombre Pelicula", max_length=200)
    descripcion_pelicula = models.TextField(verbose_name="Descripcion", max_length=500)
    categoria_pelicula = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    portada_pelicula = models.ImageField(upload_to='imagenes/', null=True, verbose_name="Portada")
    enlace_pelicula = models.TextField(verbose_name="Enlace", max_length=500)
    es_serie = False
    baja = models.DateField(verbose_name="baja")
    

class Serie(Pelicula):
    numero_capitulo= models.IntegerField(verbose_name= "Número de Capitulo",null=True)
    nombre_capitulo = models.CharField(verbose_name="Nombre del Capitulo", max_length=200)
    descripcion_capitulo = models.TextField(verbose_name="Descripcion", max_length=500)
    portada_capitulo = models.ImageField(upload_to='imagenes/', null=True, verbose_name="Portada")
    enlace_capitulo = models.TextField(verbose_name="Enlace", max_length=500)
    baja_capitulo = models.DateField(verbose_name="baja")


class Visualizaciones(models.Model):
    id_suscriptor = models.ForeignKey(Suscriptor, on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name="Fecha de vista")
    tiempo_visto = models.DurationField(verbose_name="Tiempo visto")
    
    class Meta:
        abstract=True

class Visualizaciones_peliculas(Visualizaciones):
    id_pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    

class Visualizaciones_series(Visualizaciones):
    id_serie = models.ForeignKey(Serie, on_delete=models.CASCADE)