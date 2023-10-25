from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse
from django.shortcuts import render
from datetime import datetime
from django.template import Template
from administracion.forms import FormAltaPelicula
from administracion.forms import FormAltaCategoria, FormAltaSuscriptor
from .models import Categorias, Suscriptor, Pelicula

# Create your views here.

#listado y crear peliculas

def administracion(request):
    peliculas = Pelicula.objects.all()  # Obtiene todas las pelis desde la base de datos
    return render(request, "administracion/index.html" , {'peliculas': peliculas})


def create_pelicula(request):
    context = {}
    
    if request.method == "POST":
        alta_pelicula = FormAltaPelicula()
        if create_pelicula.is_valid():
            nombre = FormAltaPelicula.cleaned_data['nombre']
            descripcion = FormAltaPelicula.cleaned_data['descripcion']
            categoria = FormAltaPelicula.cleaned_data['categoria']
            portada = FormAltaPelicula.cleaned_data['portada']
            enlace = FormAltaPelicula()
            alta_pelicula.save()
    
    else:
        alta_pelicula = FormAltaPelicula()
    
    
    context['form_alta_pelicula'] = FormAltaPelicula
    
    return render(request, 'administracion/create_pelicula.html', context)



def base_admin(request):
    return render(request, "administracion/base_admin.html")


def listado_categorias(request):
    categorias = Categorias.objects.all()  # Obtiene todas las categorías desde la base de datos
    return render(request, "administracion/listado_categorias.html", {'categorias': categorias})


def create_categoria(request):
    context = {}
    
    if request.method == "POST":
        alta_categoria = FormAltaCategoria()
    
    else:
        alta_categoria = FormAltaCategoria()
    
    
    context['form_alta_categoria'] = FormAltaCategoria
    
    return render(request, 'administracion/create_categoria.html', context)

#suscriptores

def listado_suscriptores(request):
    suscriptores = Suscriptor.objects.all()  # Obtiene todos los suscribers desde la base de datos
    return render(request, "administracion/listado_suscriptores.html", {'suscriptores': suscriptores})



def create_suscriptor(request):
    context = {}
    
    if request.method == "POST":
        alta_suscriptor = FormAltaSuscriptor()
    
    else:
        alta_suscriptor = FormAltaSuscriptor()
    
    
    context['form_alta_suscriptor'] = FormAltaSuscriptor
    
    return render(request, 'index.html', context)



