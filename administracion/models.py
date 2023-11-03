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
    baja = models.DateField(verbose_name="baja", null=True)
    
    class Meta:
        verbose_name_plural = 'Suscriptores'
        

class Categorias(models.Model):
    nombre_categoria = models.CharField(verbose_name="Nombre categoria", max_length=100)
    
    def __str__(self) -> str:
        return f'{self.nombre_categoria} '
 

class Video (models.Model):
    nombre= models.CharField(verbose_name="Nombre", max_length=200)
    descripcion = models.TextField(verbose_name="Descripcion", max_length=500)
<<<<<<< HEAD
#    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    portada = models.ImageField(upload_to='imagenes/', null=True, verbose_name="Portada")
    enlace = models.TextField(verbose_name="Enlace", max_length=500)
=======
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    portada = models.ImageField(upload_to="peliculas/", null=True, verbose_name="Portada")
    enlace = models.URLField(verbose_name="Enlace", max_length=500)
>>>>>>> fd0160b32ed2aacdb337924905747da61e6c957e
    baja = models.DateField(verbose_name="baja", null=True)
    categoria=models.ManyToManyField(Categorias)

    class Meta:
     abstract = True

class Pelicula(Video):
    suscriptor=models.ManyToManyField(Suscriptor, through="Visualizaciones_pelicula")
    
    def __str__(self) -> str:
        return f'{self.nombre} '

class Serie(Video):
    cant_capitulos= models.IntegerField(verbose_name="Cantidad de capítulos", null=True)

    def __str__(self) -> str:
        return f'{self.nombre} '

class Capitulo(Video):
    categoria = None # Elimina el campo categoria de esta clase 
    serie=models.ForeignKey(Serie, on_delete=models.CASCADE)
    numero_capitulo= models.IntegerField(verbose_name= "Número de Capitulo")
    suscriptor=models.ManyToManyField(Suscriptor, through="Visualizaciones_capitulo")
    
    def __str__(self) -> str:
        return f'{self.nombre} '

class Visualizaciones(models.Model):
    fecha = models.DateField(verbose_name="Fecha de vista")
    tiempo_visto = models.DurationField(verbose_name="Tiempo visto")

    class Meta:
        abstract = True

class Visualizaciones_pelicula(Visualizaciones):
    suscriptor=models.ForeignKey(Suscriptor, on_delete=models.CASCADE)
    pelicula=models.ForeignKey(Pelicula, on_delete=models.CASCADE)

class Visualizaciones_capitulo(Visualizaciones):
    suscriptor=models.ForeignKey(Suscriptor, on_delete=models.CASCADE)
    capitulo=models.ForeignKey(Capitulo, on_delete=models.CASCADE)