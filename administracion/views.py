from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError, HttpRequest
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from django.template import Template
from administracion.forms import FormAltaCategoria, SuscriptorForm, FormEditCategoria, registerForm, PlanForm
from .models import Categorias, Suscriptor, Pelicula, Serie
from django.contrib import messages
from django.urls import reverse_lazy
from typing import Any
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User, Group


from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from administracion.forms import SerieForm, PeliculaForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def administracion(request):
    return render(request, "administracion/index.html" )

#listado y crear peliculas


#Tradicional de Django

def listado_peliculas(request):
    peliculas = Pelicula.objects.all() 
    return render(request, "administracion/listado_peliculas.html", {'peliculas': peliculas})

#Vista basada en Clase

class CategoriasListView(ListView):
    model = Categorias
    context_object_name = 'categorias'
    template_name = 'administracion/listado_categorias.html'
    ordering = ['nombre_categoria']

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any):
        if 'nombre_categoria' in request.GET:
            self.queryset = self.queryset.filter(nombre_categoria__contains=request.GET['nombre_categoria'])

        return super().get(request, *args, **kwargs)


class CategoriasCreateView(CreateView):
    model = Categorias
    fields = ['nombre_categoria']
    #form_class = FormAltaCategoria
    template_name = 'administracion/create_categoria.html'
    success_url = reverse_lazy('listado_categorias')


class CategoriaUpdateView(UpdateView):
    model = Categorias
    fields = ['nombre_categoria']
    #form_class = FormAltaCategoria
    template_name = 'administracion/create_categoria.html'
    success_url = reverse_lazy('listado_categorias')


class CategoriasDeleteView(DeleteView):
    model = Categorias
    template_name = 'administracion/eliminar_categoria.html'
    success_url = reverse_lazy('listado_categorias')


#Peliculas

def pelicula_crear(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            p1 = Pelicula(
                nombre=form.cleaned_data.get('nombre'),
                descripcion=form.cleaned_data.get('descripcion'),
                categoria = form.cleaned_data.get('categoria'),
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
            pelicula.categoria =  data['categoria']
            pelicula.portada = data['portada']
            pelicula.enlace = data['enlace']

            pelicula.save()
            return redirect('listado_peliculas')
    else:
        form = PeliculaForm(initial={
            'nombre': pelicula.nombre, 
            'descripcion': pelicula.descripcion, 
            'categoria': pelicula.categoria,
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
             #'categoria': form.categoria,
            'portada': form.portada, 
            'enlace': form.enlace, 
  
            })
    return render(request, 'administracion/eliminar_pelicula.html', {'form': form})



def base_admin(request):
    return render(request, "administracion/base_admin.html")

def plan_crear(request):
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administracion')
    else:
        form = PlanForm()

    return render(request, 'administracion/plan_crear.html', {'form': form})

'''
#Categorias al old school django, funciona ok

def listado_categorias(request):
    categorias = Categorias.objects.all()  # Obtiene todas las categorías desde la base de datos
    return render(request, "administracion/listado_categorias.html", {'categorias': categorias})



def create_categoria(request):
    context = {}
    
    if request.method == "POST":
        form = FormAltaCategoria(request.POST) 
        if form.is_valid():
            # Guardamos datos en la ddbb
            nombre_categoria = form.cleaned_data['nombre_categoria']
            nueva_categoria = Categorias(nombre_categoria=nombre_categoria)
            nueva_categoria.save()
            
            # Procesar el formulario si categoria es válida
            return redirect('listado_categorias')
        else:
            # Error en el formulario
            context['form_errors'] = form.errors
    else:
        form = FormAltaCategoria()
    
    context['form'] = form
    
    return render(request, 'administracion/create_categoria.html', context)

def categoria_editar(request, pk):
    categoria = Categorias.objects.get(id=pk)
    if request.method == 'POST':
        form = FormAltaCategoria(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            categoria.nombre_categoria =data['nombre_categoria']
            categoria.save()
            return redirect('listado_categorias')
    else:
        form = FormAltaCategoria(initial={
            'nombre_categoria': categoria.nombre_categoria, 
            
            })
    return render(request, 'administracion/create_categoria.html', {'form': form})



def categoria_eliminar(request,pk):
    form = Categorias.objects.get(id=pk)
    if request.method == 'POST':
        form.delete()
        return redirect('listado_categorias')
    else:
        form = FormAltaCategoria(initial={
            'nombre': form.nombre_categoria, 

            })
    return render(request, 'administracion/eliminar_categoria.html', {'form': form})
'''

#series

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
#                categoria =  Categorias.objects.get(id=form.cleaned_data.get('categoria')),
                categoria =  form.cleaned_data.get('categoria'),
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
            # try:
            #     categ=Categorias.objects.get(pk=data['categoria'])
            # except Categorias.DoesNotExist:
            #     return render(request, 'administracion/404_admin.html')
            serie.nombre =data['nombre']
            serie.descripcion = data['descripcion']
            serie.categoria =  data['categoria']
            serie.portada = data['portada']
            serie.enlace = data['enlace']
            serie.cant_capitulos=data['cant_capitulos']

            serie.save()
            return redirect('serie_lista')
    else:
        form = SerieForm(initial={
            'nombre': serie.nombre, 
            'descripcion': serie.descripcion, 
            'categoria': serie.categoria,
            'portada': serie.portada, 
            'enlace': serie.enlace, 
            'cant_capitulos': serie.cant_capitulos
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
            'categoria': form.categoria,
            'portada': form.portada, 
            'enlace': form.enlace, 
            'cant_capitulos': form.cant_capitulos
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
            nombre_apellido = alta_suscriptor.cleaned_data['nombreApellido']
            dni = alta_suscriptor.cleaned_data['dni']
            email = alta_suscriptor.cleaned_data['email']
            fecha_inicio = alta_suscriptor.cleaned_data['fecha_inicio']
            username = alta_suscriptor.cleaned_data['username']
            password1 = alta_suscriptor.cleaned_data['password1']
            password2 = alta_suscriptor.cleaned_data['password2']
            
            # Creo una instancia de Suscriptor
            nuevo_suscriptor = Suscriptor(nombre_apellido=nombre_apellido, dni=dni, email=email, fecha_inicio=fecha_inicio, username= username, password1=password1, password2=password2)
            nuevo_suscriptor.save()
            #crea el suscriptor como user y lo asigna al grupo
            nuevo_usuario = User.objects.create_user(username=username, password=password1)
            grupo, creado = Group.objects.get_or_create(name='suscriptor')
            grupo.user_set.add(nuevo_usuario)

            messages.success(request, 'Gracias!Su registro fue exitoso')
            return render(request, 'index.html')           
           
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
             if form.is_valid():
                data = form.cleaned_data
                suscriptor.nombre_apellido =data['nombreApellido']
                suscriptor.dni = data['dni']
                suscriptor.email = data['email']
                suscriptor.fecha_inicio = data['fecha_inicio']
 
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
    return render(request, 'administracion/suscriptor_crear.html', {'form': form})

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

#Login usuario


def register(request):
    contexto = {}
    if request.method == "POST":
        form = registerForm(request.POST)  # Paso request.POST al form
        if form.is_valid():
            # Guardo datos del formulario en la ddbb
            nombre_apellido = form.cleaned_data['nombreApellido']
            dni = form.cleaned_data['dni']
            email = form.cleaned_data['email']
            fecha_inicio = form.cleaned_data['fecha_inicio']
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            
            # Creo una instancia de Suscriptor
            nuevo_user = Suscriptor(nombre_apellido=nombre_apellido, dni=dni, email=email, fecha_inicio=fecha_inicio, username= username, password1 = password1, password2=password2)
            nuevo_user.save()
            return render(request, 'administracion/register.html')           
           
        else:
            # Errores en el formulario
            contexto['form_errors'] =  form.errors
    else:
         form = registerForm()
    
    contexto['form'] =  form
    
    return render(request, 'administracion/register.html', contexto)
    
    
    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Bienvenido/a, {username}')
                return redirect('index')  #LLeva a la home del sitio
            else:
                messages.error(request, f'Has ingresado un dato erroneo, intenta nuevamente')
        else:
            messages.error(request, 'Por favor, ingresa un nombre de usuario y una contraseña válidos.')

    form = AuthenticationForm()
    return render(request, 'administracion/login.html', {'form': form, 'title': 'Log in'})


def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión correctamente.')
    return redirect('login')
