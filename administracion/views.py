from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from datetime import datetime
from django.template import Template
from administracion.forms import FormAltaPelicula
from administracion.forms import FormAltaCategoria, FormAltaSuscriptor
from .models import Categorias, Suscriptor, Pelicula
from .forms import FormAltaCategoria
from django.contrib import messages

# Create your views here.

#listado y crear peliculas

def administracion(request):
    peliculas = Pelicula.objects.all()  # Obtiene todas las pelis desde la base de datos
    return render(request, "administracion/index.html" , {'peliculas': peliculas})


def create_pelicula(request):
    context = {}
    
    if request.method == "POST":
        alta_pelicula = FormAltaPelicula(request.POST) #paso request al form
        if alta_pelicula.is_valid():
            #Guardo en a ddbb
            nombre = alta_pelicula.cleaned_data['nombre']
            descripcion = alta_pelicula.cleaned_data['descripcion']
            categoria = alta_pelicula.cleaned_data['categoria']
            portada = alta_pelicula.cleaned_data['portada']
            enlace = alta_pelicula.cleaned_data['enlace']
            
            # Creo instancia de Pelicula y guardar
            nueva_pelicula = Pelicula(nombre=nombre, descripcion=descripcion, categoria=categoria, portada=portada, enlace=enlace)
            nueva_pelicula.save()
        else:
            return redirect('administracion/listado_peliculas.html')  # Redirige a la página del listado peliculas

    
    
    else:
        alta_pelicula = FormAltaPelicula()
    
    context['form_alta_pelicula'] = alta_pelicula
    
    return render(request, 'administracion/create_pelicula.html', context)



def base_admin(request):
    return render(request, "administracion/base_admin.html")


def listado_categorias(request):
    categorias = Categorias.objects.all()  # Obtiene todas las categorías desde la base de datos
    return render(request, "administracion/listado_categorias.html", {'categorias': categorias})



def create_categoria(request):
    context = {}
    
    if request.method == "POST":
        alta_categoria = FormAltaCategoria(request.POST)  # Pasamos request al form
        if alta_categoria.is_valid():
            # Guardamos datos en la ddbb
            nombre_categoria = alta_categoria.cleaned_data['nombre_categoria']
            nueva_categoria = Categorias(nombre_categoria=nombre_categoria)
            nueva_categoria.save()
            
            # Procesar el formulario si la edad es válida
            
        else:
            # Error en el formulario
            context['form_errors'] = alta_categoria.errors
    else:
        alta_categoria = FormAltaCategoria()
    
    context['form_alta_categoria'] = alta_categoria
    
    return render(request, 'administracion/create_categoria.html', context)


#suscriptores

def listado_suscriptores(request):
    suscriptores = Suscriptor.objects.all()  # Obtiene todos los suscribers desde la base de datos
    return render(request, "administracion/listado_suscriptores.html", {'suscriptores': suscriptores})


def create_suscriptor(request):
    context = {}

    if request.method == "POST":
        alta_suscriptor = FormAltaSuscriptor(request.POST)  # Paso request.POST al form
        if alta_suscriptor.is_valid():
            # Guardo datos del formulario en la ddbb
            nombreApellido = alta_suscriptor.cleaned_data['nombreApellido']
            dni = alta_suscriptor.cleaned_data['dni']
            email = alta_suscriptor.cleaned_data['email']

            # Creo una instancia de Suscriptor
            nuevo_suscriptor = Suscriptor(nombreApellido=nombreApellido, dni=dni, email=email)
            nuevo_suscriptor.save()
           
        else:
            # Errores en el formulario
            context['form_errors'] = alta_suscriptor.errors
    else:
        alta_suscriptor = FormAltaSuscriptor()
    
    context['form_alta_suscriptor'] = alta_suscriptor
    
    return render(request, 'alta_suscriptor.html', context)
