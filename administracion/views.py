from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse
from django.shortcuts import render
from datetime import datetime
from django.template import Template
from administracion.forms import FormAltaPelicula
from administracion.forms import FormAltaCategoria

# Create your views here.
def administracion(request):
    return render(request, "administracion/index.html")


def base_admin(request):
    return render(request, "administracion/base_admin.html")


def listado_categorias(request):
    return render(request, "administracion/listado_categorias.html")


def create_pelicula(request):
    context = {}
    
    if request.method == "POST":
        alta_pelicula = FormAltaPelicula()
    
    else:
        alta_pelicula = FormAltaPelicula()
    
    
    context['form_alta_pelicula'] = FormAltaPelicula
    
    return render(request, 'administracion/create_pelicula.html', context)


def create_categoria(request):
    context = {}
    
    if request.method == "POST":
        alta_categoria = FormAltaCategoria()
    
    else:
        alta_categoria = FormAltaCategoria()
    
    
    context['form_alta_categoria'] = FormAltaCategoria
    
    return render(request, 'administracion/create_categoria.html', context)

