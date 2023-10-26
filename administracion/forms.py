import re
from django import forms
from django.core.exceptions import ValidationError


class FormAltaPelicula(forms.Form):
    nombre_pelicula = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre de la pelicula'}))
    descripcion_pelicula = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Solo texto'}))
    categoria_pelicula = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre de categoria'}))
    portada_pelicula = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese url de imagen'}))
    enlace_pelicula = forms.URLField(required = True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese url de enlace'}))
    
    
class FormAltaCategoria(forms.Form):
    nombre_categoria = forms.CharField(label='Nombre categoría:', required=True,
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre de la nueva categoria, ej: Drama'})
    )
    
    

class FormAltaSuscriptor(forms.Form):
    nombreApellido = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre completo'}))
    dni = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su DNI'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su mail'}))