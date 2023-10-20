import re
from django import forms
from django.core.exceptions import ValidationError


class FormAltaPelicula(forms.Form):
    nombre = forms.CharField(max_length=100)
    categoria = forms.CharField(max_length=100)