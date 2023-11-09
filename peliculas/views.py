from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse
from django.shortcuts import render
from datetime import datetime
from django.template import Template
from administracion.models import Pelicula, Serie, Video
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def peliculas(request):
    peliculas = Pelicula.objects.all()  # Obtiene todas las películas desde la base de datos
    context = {
        'peliculas': peliculas, 
        'es_suscriptor': True,
        'usuario_conectado': True,
        'nombre_usuario': 'Genérico',
    }
    return render(request, "peliculas.html", context)



def detallepelicula(request):
    return render(request, "detallepelicula.html")
    
def archivo(request, year):
    if year == 2028:
        url = reverse("index")
        return HttpResponseRedirect(url)
    elif year == 2027:
        return HttpResponseServerError("<h1> Error de servidor </h1>")
    
    return HttpResponse(f'<h1>Peliculas de archivo del anio: {year}</h1>')



@login_required
def series(request):
    series = Serie.objects.all()  # Obtiene todas las series desde la base de datos
    context = {
        'series': series, 
        'es_suscriptor': True,
        'usuario_conectado': True,
        'nombre_usuario': 'Genérico',
    }
    return render(request, "series.html", context)