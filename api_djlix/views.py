from django.shortcuts import render
from rest_framework import viewsets, permissions
from api_djlix import serializers
from administracion.models import Pelicula


# Create your views here.

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = serializers.PeliculaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


