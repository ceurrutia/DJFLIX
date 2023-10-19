import re
from django import forms
from django.core.exceptions import ValidationError
from administracion import forms

class FormcreatePelicula(forms.Form):
    CATEGORIA = (
        ('', '-Seleccione-'),
        (1, 'Drama'),
        (2, 'Accion'),
        (3, 'Aventura'),
    )
    nombre = forms.CharField(
        label="Nombre de la pelicula",
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa nombre de la pelicula'})
        )
    fecha_estreno = forms.DateField(
        label="Fecha de estreno ",  
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa la fecha de estreno'})
        )
    descripcion = forms.Textarea(
        label="Descripcion", 
        max_lenght=500, 
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Coloca descripcion hasta 500 caracteres'})
        )
    duracion = forms.DateTimeField(
        label="Duracion", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa la duracion' })
        )
    categoria = forms.ChoiceField(
        label='Selecciona categoria',
        choices=CATEGORIA,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    clasificacion = forms.CharField(
        label="clasificacion", 
        required=False, 
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escriba clasificacion'})
        )
    portada = forms.textInput( 
        label = "portada",
        required = True,
        widget=forms.forms.URLField(attrs={'class': 'form-control', 'placeholder': 'Ingresa la duracion' })
        )