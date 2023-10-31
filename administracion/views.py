from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from django.template import Template
from administracion.forms import FormAltaCategoria, SuscriptorForm, FormEditCategoria
from .models import Categorias, Suscriptor, Pelicula, Serie
from django.contrib import messages

from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from administracion.forms import SerieForm, PeliculaForm

# Create your views here.

def administracion(request):
    return render(request, "administracion/index.html" )

#listado y crear peliculas


#Tradicional de Django

def listado_peliculas(request):
    peliculas = Pelicula.objects.all() 
    return render(request, "administracion/listado_peliculas.html", {'peliculas': peliculas})

#Vista basada en Clase

'''
class PeliculasListView(ListView):
    
    model = Pelicula
    context_object_name = 'peliculas'
    template_name = 'administracion/listado_peliculas.html'
    ordering = ['id']
'''


def pelicula_crear(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            p1 = Pelicula(
                nombre=form.cleaned_data.get('nombre'),
                descripcion=form.cleaned_data.get('descripcion'),
                categoria=get_object_or_404(Categorias, id=form.cleaned_data.get('categoria')),
                portada=form.cleaned_data.get('portada'),
                enlace=form.cleaned_data.get('enlace'),
            )
            p1.save()
            return redirect('listado_peliculas')
    else:
        form = PeliculaForm()
    return render(request, 'administracion/create_pelicula.html', {'form': form})


def pelicula_editar(request, pk):
    pelicula = Pelicula.objects.get(id=pk)
    if request.method == 'POST':
        form =PeliculaForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            pelicula.nombre = data['nombre']
            pelicula.descripcion = data['descripcion']
            #pelicula.categoria =  Categorias.objects.get(id=data['categoria']),
            pelicula.portada = data['portada']
            pelicula.enlace = data['enlace']

            pelicula.save()
            return redirect('listado_peliculas')
    else:
        form = PeliculaForm(initial={
            'nombre': pelicula.nombre, 
            'descripcion': pelicula.descripcion, 
            'portada': pelicula.portada, 
            'enlace': pelicula.enlace,
            })
    return render(request, 'administracion/create_pelicula.html', {'form': form})

def pelicula_eliminar(request,pk):
    form = Pelicula.objects.get(id=pk)
    if request.method == 'POST':
        form.delete()
        return redirect('listado_peliculas')
    else:
        form = PeliculaForm(initial={
            'nombre': form.nombre, 
            'descripcion': form.descripcion, 
 #           'categoria': form.categoria,
            'portada': form.portada, 
            'enlace': form.enlace, 
  
            })
    return render(request, 'administracion/eliminar_pelicula.html', {'form': form})



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

def serie_editar(request, pk):
    serie = Serie.objects.get(id=pk)
    if request.method == 'POST':
        form = SerieForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            serie.nombre =data['nombre']
            serie.descripcion = data['descripcion']
#            serie.categoria =  Categorias.objects.get(id=data['categoria']),
            serie.portada = data['portada']
            serie.enlace = data['enlace']
 #           serie.cant_capitulos=data['cant_capitulos']

            serie.save()
            return redirect('serie_lista')
    else:
        form = SerieForm(initial={
            'nombre': serie.nombre, 
            'descripcion': serie.descripcion, 
 #           'categoria': serie.categoria,
            'portada': serie.portada, 
            'enlace': serie.enlace, 
  #          'cant_capitulos': serie.cant_capitulos
            })
    return render(request, 'administracion/serie_crear.html', {'form': form})

def serie_eliminar(request,pk):
    form = Serie.objects.get(id=pk)
    if request.method == 'POST':
        form.delete()
        return redirect('serie_lista')
    else:
        form = SerieForm(initial={
            'nombre': form.nombre, 
            'descripcion': form.descripcion, 
 #           'categoria': form.categoria,
            'portada': form.portada, 
            'enlace': form.enlace, 
  #          'cant_capitulos': form.cant_capitulos
            })
    return render(request, 'administracion/serie_eliminar.html', {'form': form})

#suscriptores

def listado_suscriptores(request):
    suscriptores = Suscriptor.objects.all()  # Obtiene todos los suscribers desde la base de datos
    return render(request, "administracion/listado_suscriptores.html", {'suscriptores': suscriptores})


def create_suscriptor(request):
    context = {}

    if request.method == "POST":
        alta_suscriptor = SuscriptorForm(request.POST)  # Paso request.POST al form
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
        alta_suscriptor = SuscriptorForm()
    
    context['form_alta_suscriptor'] = alta_suscriptor
    
    return render(request, 'alta_suscriptor.html', context)


def suscriptor_editar(request, pk):
    suscriptor = Suscriptor.objects.get(id=pk)
    if request.method == 'POST':
        form =SuscriptorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            suscriptor.nombre_apellido = data['nombre_apellido']
            suscriptor.dni = data['dni']
            suscriptor.email = data['email']
            suscriptor.fecha_inicio = data['fecha_inicio']
            suscriptor.baja = data['baja']

            suscriptor.save()
            return redirect('listado_suscriptores')
    else:
        form = SuscriptorForm(initial={
            'nombreApellido': suscriptor.nombre_apellido, 
            'dni': suscriptor.dni, 
            'email': suscriptor.email,
            'fecha_inicio' : suscriptor.fecha_inicio,
            'baja': suscriptor.baja 
            })
    return render(request, 'administracion/listado_suscriptores.html', {'form': form})

def suscriptor_eliminar(request,pk):
    form = Suscriptor.objects.get(id=pk)
    if request.method == 'POST':
        form.delete()
        return redirect('listado_suscriptores')
    else:
        form = PeliculaForm(initial={
            'nombre': form.nombre_apellido, 
            'dni': form.dni, 
            'email': form.email,  
            'fecha_inicio' : form.fecha_inicio,
            'baja': form.baja
  
            })
    return render(request, 'administracion/suscriptor_eliminar.html', {'form': form})