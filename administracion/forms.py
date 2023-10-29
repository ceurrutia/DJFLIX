import re
from django import forms
from django.core.exceptions import ValidationError
from .models import Categorias

class FormAltaPelicula(forms.Form):
    lista_categorias=[]
    for categoria in Categorias.objects.all():
        lista_categorias.append((categoria.id, categoria.nombre_categoria))
    nombre_pelicula = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre de la pelicula'}))
    descripcion_pelicula = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Solo texto'}))
    categoria_pelicula = forms.ChoiceField(choices=lista_categorias)
    portada_pelicula = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese url de imagen'}))
    enlace_pelicula = forms.URLField(required = True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese url de enlace'}))
    
class FormAltaCategoria(forms.Form):
    nombre_categoria = forms.CharField(label='Nombre categoría:', required=True,
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre de la nueva categoria, ej: Drama'})
    )
    
    
class FormEditCategoria(forms.Form):
    nombre_categoria = forms.CharField(label = 'nombre categoria', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nuevo nombre de la  categoria'}) )  
    
    def __init__(self, *args, **kwargs):
        
        super(FormEditCategoria, self).__init__(*args, **kwargs)
        self.fields['nombre_categoria'].widget.attrs.update({'class': 'form-control'})



class FormAltaSuscriptor(forms.Form):
    nombreApellido = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre completo'}))
    dni = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su DNI'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su mail'}))
    fecha_inicio=forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese fecha de inicio'}))