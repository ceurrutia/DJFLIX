from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.template import Template
from administracion.models import Pelicula, Serie, Video
from django.contrib.auth.decorators import login_required, user_passes_test
from .decorators import group_required , group_required_or_staff


# Create your views here.

@login_required
@group_required_or_staff ('suscriptor')
def peliculas(request):
    peliculas = Pelicula.objects.all()
    for pelicula in peliculas:
        pelicula.enlace = f'https://www.youtube.com/embed/{pelicula.enlace}'
    context = {
        'peliculas': peliculas, 
        'es_suscriptor': True,
        'usuario_conectado': True,
        'nombre_usuario': 'Genérico',
    }
    return render(request, "peliculas.html", context)



@login_required
@group_required_or_staff('suscriptor')
def detallepelicula(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, pk=pelicula_id)
    context = {
        'pelicula': pelicula,
    }
    return render(request, 'detallepelicula.html', context)
    
def archivo(request, year):
    if year == 2028:
        url = reverse("index")
        return HttpResponseRedirect(url)
    elif year == 2027:
        return HttpResponseServerError("<h1> Error de servidor </h1>")
    elif year == 2024:
        return HttpResponseServerError("<h1> Quisi mamaaaaaa. Cortaste toda la loz </h1>")
    else:
        return render(request, 'archivo.html')
    #return HttpResponse(f'<h1>Peliculas de archivo del año: {year}</h1>')


@login_required
@group_required_or_staff('suscriptor')
def series(request):
    series = Serie.objects.all()
    for serie in series:
        serie.enlace = f'https://www.youtube.com/embed/{serie.enlace}'
    context = {
        'series': series, 
        'es_suscriptor': True,
        'usuario_conectado': True,
        'nombre_usuario': 'Genérico',
    }
    return render(request, "series.html", context)

@login_required
@group_required_or_staff('suscriptor')
def detalleserie(request, serie_id):
    serie = get_object_or_404(Serie, pk=serie_id)
    context = {
        'serie': serie,
    }
    return render(request, 'detalleserie.html', context)