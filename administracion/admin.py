from typing import Any
from django.contrib import admin
from django.db.models.fields.related import ManyToManyField
from django.forms.models import ModelMultipleChoiceField
from django.http.request import HttpRequest
from administracion.models import Pelicula, Serie,Capitulo,  Suscriptor, Categorias, Visualizaciones_pelicula, Visualizaciones_capitulo


# Register your models here.

#admin.site.register(Pelicula)
admin.site.register(Serie)
admin.site.register(Capitulo)
admin.site.register(Visualizaciones_pelicula)
admin.site.register(Visualizaciones_capitulo)
#admin.site.register(Suscriptor)
admin.site.register(Categorias)

# admin.py
#Pelicula
#    Suscriptor
#Libro
#    autor
class SuscriptorInline(admin.TabularInline):
    model = Pelicula.suscriptor.through  # Modelo de la relación muchos a muchos

class PeliculaAdmin(admin.ModelAdmin):
    inlines = [SuscriptorInline,]
    filter_horizontal = ('suscriptor',)

admin.site.register(Suscriptor)
admin.site.register(Pelicula, PeliculaAdmin)
