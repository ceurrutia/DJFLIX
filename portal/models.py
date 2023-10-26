from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

TIPO_CONSULTA = (
('', '-Seleccione-'),
(1, 'Soporte'),
(2, 'Consultas sobre peliculas o series'),
(3, 'Trabajar en DJflix'),
)

# Create your models here.
class Contacto(models.Model):
    nombre_y_apellido= models.CharField(verbose_name="Nombre y apellido", max_length=250)
    edad= models.IntegerField(verbose_name= "Edad")
    telefono= models.IntegerField(verbose_name="Teléfono")
    email= models.EmailField(verbose_name="Email", max_length=250)
    tipo_de_consulta= models.IntegerField(verbose_name= "Tipo de consulta", choices=TIPO_CONSULTA)
    mensaje = models.TextField(verbose_name="Mensaje", max_length=500)
    fecha_y_hora = models.DateTimeField(verbose_name="Fecha y hora", null=True,default=timezone.now)
    se_envio_email= models.BooleanField(verbose_name="se_envio_email", default=False)

    def __str__(self):
        return f'{self.nombre_y_apellido} - {self.email} - {self.mensaje}'