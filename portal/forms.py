import re
from django import forms
from django.core.exceptions import ValidationError


def custom_validate_email(value):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, value):
        raise ValidationError('Correo electrónico inválido')

def clean_edad(self):
    if self.cleaned_data['edad'] < 18:
        raise ValidationError('El usuario no puede tener menos de 18 años')

class contactForm(forms.Form):
    TIPO_CONSULTA = (
        ('', '-Seleccione-'),
        (1, 'Soporte'),
        (2, 'Consultas sobre peliculas o series'),
        (3, 'Trabajar en DJflix'),
    )
    nombreApellido = forms.CharField(
        label="Nombre y apellido",
        max_length=20, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu nombre y Apellido'})
        )
    mail = forms.EmailField(
        label="Email ", 
        required= True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu email'})
        )
    edad = forms.IntegerField(
        label="Edad", 
        min_value=18, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu edad'})
        )
    telefono = forms.IntegerField(
        label="Telefono", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu telefono' })
        )
    tipo_consulta = forms.ChoiceField(
        label='Tipo de consulta',
        choices=TIPO_CONSULTA,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    mensaje = forms.CharField(
        label="Mensaje", 
        required=False, 
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe aqui tu consulta'})
        )
    recibir_mail = forms.BooleanField(required=False, 
        label="Quiero recibir por e-mail la informacion que estoy completando", 
        initial=True,
        widget=forms.CheckboxInput(attrs={})
        )   
