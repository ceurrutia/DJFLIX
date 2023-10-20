from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre_apellido = models.CharField(verbose_name='Nombre y Apellido', max_length=500)
    direccion = models.CharField(verbose_name='Direccion', max_length=700)
    dni = models.TextField(verbose_name= "DNI", max_length=350)
    email = models.EmailField(verbose_name="Email", max_length=250)
    pais = models.CharField(verbose_name='Pais', max_length=200)
    ciudad = models.CharField(verbose_name='Ciudad', max_length=200)

    def __str__(self) -> str:
        return f'{self.nombre_apellido} - {self.dni} - {self.direccion}  -  {self.email} - {self.pais} - {self.ciudad} '
 
    class Meta:
     abstract = True
    
class Suscripcion(models.Model):
        tipo_plan = models.CharField(verbose_name="Tipo de Plan", max_length=150)
        baja = models.DateField(verbose_name="baja")
        
def __str__(self) -> str:
        return f'{self.tipo_plan} -{self.baja}'
          
class Suscriptor(Persona):
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")
    tipo_plan = models.ForeignKey(Suscripcion, on_delete=models.CASCADE)
   
class Categorias(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=100)

class Peliculas(models.Model):
    nombre = models.CharField(verbose_name="Nombre Pelicula", max_length=200)
    fecha_estreno = models.DateField(verbose_name="Fecha de estreno")
    descripcion = models.TextField(verbose_name="Descripcion", max_length=500)
    portada = models.ImageField(upload_to='imagenes/', null=True, verbose_name="Portada")
    duracion = models.DateTimeField(verbose_name="Duracion")
    clasificacion = models.CharField(verbose_name= "Clasificacion", max_length=250)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    es_serie = False
    enlace = models.TextField(verbose_name="Enlace", max_length=500)
    suscriptor = models.ManyToManyField(Suscriptor, through="Visualizaciones")
    baja = models.DateField(verbose_name="baja")

class Capitulos()
    capitulo_numero= models.IntegerField(verbose_name= "Capitulo Número",null=True)
    nombre_capitulo = models.CharField(verbose_name="Nombre del Capitulo", max_length=200)
    id_pelicula = models.ForeignKey(Peliculas, on_delete=models.CASCADE)
    descripcion = models.TextField(verbose_name="Descripcion", max_length=500)
    portada = models.ImageField(upload_to='imagenes/', null=True, verbose_name="Portada")
    duracion = models.DateTimeField(verbose_name="Duracion")
    enlace = models.TextField(verbose_name="Enlace", max_length=500)
    baja = models.DateField(verbose_name="baja")

class Visualizaciones(models.Model):
    id_suscriptor = models.ForeignKey(Suscriptor, on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name="Fecha de vista")
    tiempo_visto = models.DurationField(verbose_name="Tiempo visto")
    
    class Meta:
        abstract=True

class Visualizaciones_peliculas(Visualizaciones):
    id_pelicula = models.ForeignKey(Peliculas, on_delete=models.CASCADE)

class Visualizaciones_capitulo(Visualizaciones):
    id_capitulo = models.ForeignKey(Capitulos, on_delete=models.CASCADE)