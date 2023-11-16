from rest_framework import serializers
from administracion.models import Pelicula

class PeliculaSerializer(serializers.ModelSerializer):
    class Meta :
        model = Pelicula
        fields = ['id', 'nombre', 'descripcion', 'categoria', 'portada', 'enlace', 'baja']
        