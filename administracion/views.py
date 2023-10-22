from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse
from django.shortcuts import render
from datetime import datetime
from django.template import Template
from administracion.forms import FormAltaPelicula
from administracion.forms import FormAltaCategoria, FormAltaSuscriptor

# Create your views here.

#listado y crear peliculas

def administracion(request):
    return render(request, "administracion/index.html")


def create_pelicula(request):
    context = {}
    
    if request.method == "POST":
        alta_pelicula = FormAltaPelicula()
    
    else:
        alta_pelicula = FormAltaPelicula()
    
    
    context['form_alta_pelicula'] = FormAltaPelicula
    
    return render(request, 'administracion/create_pelicula.html', context)



def base_admin(request):
    return render(request, "administracion/base_admin.html")

#Categorias

def listado_categorias(request):
    return render(request, "administracion/listado_categorias.html")


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
    return render(request, "administracion/listado_suscriptores.html")



def create_suscriptor(request):
    context = {}
    
    if request.method == "POST":
        alta_suscriptor = FormAltaSuscriptor()
    
    else:
        alta_suscriptor = FormAltaSuscriptor()
    
    
    context['form_alta_suscriptor'] = FormAltaSuscriptor
    
    return render(request, 'index.html', context)



