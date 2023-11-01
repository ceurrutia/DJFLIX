from django.contrib import admin
from administracion.models import Pelicula, Serie, Suscriptor, Categorias


# Register your models here.

admin.site.register(Pelicula)
admin.site.register(Serie)
admin.site.register(Suscriptor)
admin.site.register(Categorias)

