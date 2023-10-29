from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse
from django.shortcuts import render, redirect
from datetime import datetime
from django.template import Template
from administracion.forms import FormAltaPelicula
from administracion.forms import FormAltaCategoria, FormAltaSuscriptor, FormEditCategoria
from .models import Categorias, Suscriptor, Pelicula, Serie
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from administracion.forms import SerieForm

# Create your views here.

#listado y crear peliculas

'''
Tradicional de Django

def administracion(request):
    peliculas = Pelicula.objects.all()  # Obtiene todas las pelis desde la base de datos
    return render(request, "administracion/index.html" , {'peliculas': peliculas})
'''
#Vista basada en Clase

class PeliculasListView(ListView):
    
    model = Pelicula
    context_object_name = 'peliculas'
    template_name = 'administracion/index.html'
    ordering = ['id']



def create_pelicula(request):
    context = {}
    
    if request.method == "POST":
        alta_pelicula = FormAltaPelicula(request.POST) #paso request al form
        if alta_pelicula.is_valid():
            #Guardo en a ddbb
            nombre_pelicula = alta_pelicula.cleaned_data['nombre_pelicula']
            descripcion_pelicula = alta_pelicula.cleaned_data['descripcion_pelicula']
            categoria_pelicula = alta_pelicula.cleaned_data['categoria_pelicula']
            portada_pelicula = alta_pelicula.cleaned_data['portada_pelicula']
            enlace_pelicula = alta_pelicula.cleaned_data['enlace_pelicula']
            
            # Creo instancia de Pelicula y guardar
            nueva_pelicula = Pelicula(nombre_pelicula=nombre_pelicula, descripcion_pelicula=descripcion_pelicula, categoria_pelicula=categoria_pelicula, portada_pelicula=portada_pelicula ,  enlace_pelicula= enlace_pelicula)
            nueva_pelicula.save()
            
            messages.success(request, "Se ha creado una pelicula nueva")
            
        else:
#            return redirect('administracion/create_pelicula.html')
            return redirect('administracion/create_pelicula.html')
          
    else:
        alta_pelicula = FormAltaPelicula()
    
    context['form_alta_pelicula'] = alta_pelicula
    
#    return render(request, 'administracion/create_pelicula.html', context)
    return render(request, 'administracion/create_pelicula.html', context)



def base_admin(request):
    return render(request, "administracion/base_admin.html")


def listado_categorias(request):
    categorias = Categorias.objects.all()  # Obtiene todas las categorías desde la base de datos
    return render(request, "administracion/listado_categorias.html", {'categorias': categorias})



def create_categoria(request):
    context = {}
    
    if request.method == "POST":
        alta_categoria = FormAltaCategoria(request.POST) 
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

def serie_lista(request):
    series = Serie.objects.all() 
    return render(request, "administracion/serie_lista.html", {'serie': series})


def serie_crear(request):
    if request.method == 'POST':
        form = SerieForm(request.POST)
        if form.is_valid():
            s1= Serie(
                nombre =form.cleaned_data.get('nombre'),
                descripcion = form.cleaned_data.get('descripcion'),
                categoria =  Categorias.objects.get(id=form.cleaned_data.get('categoria')),
                portada = form.cleaned_data.get('portada'),
                enlace = form.cleaned_data.get('enlace'),
                cant_capitulos=0
            )
            s1.save()
            return redirect('serie_lista')
    else:
        form = SerieForm()
    return render(request, 'administracion/serie_crear.html', {'form': form})

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
            fecha_inicio = alta_suscriptor.cleaned_data['fecha_inicio']
            
            # Creo una instancia de Suscriptor
            nuevo_suscriptor = Suscriptor(nombre_apellido=nombreApellido, dni=dni, email=email, fecha_inicio=fecha_inicio)
            nuevo_suscriptor.save()
            return render(request, 'alta_suscriptor.html')           
           
        else:
            # Errores en el formulario
            context['form_errors'] = alta_suscriptor.errors
    else:
        alta_suscriptor = FormAltaSuscriptor()
    
    context['form_alta_suscriptor'] = alta_suscriptor
    
    return render(request, 'alta_suscriptor.html', context)
