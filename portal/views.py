from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError, HttpResponseBadRequest
from django.urls import reverse
from django.shortcuts import render, redirect
#from django.template import loader
from datetime import datetime
from django.template import Template
from portal.forms import contactForm
from django.contrib import messages
from django.core.exceptions import ValidationError


# Create your views here.
def index(request):
    
   # indexTemplate = loader.get_template("index.html")
   # contexto = {"ahora": datetime.now}
   # indexTemplate_renderizado = indexTemplate.render(contexto, request)
   # respuesta = HttpResponse(indexTemplate_renderizado)
   return render(request, "index.html", {"ahora":datetime.now()})


def contacto(request):
    if request.method == 'GET':
        #No impacta en el sistema
        formulario_contacto = contactForm()
        
    elif request.method == 'POST':
        #Instancia de un formulario con datos
        #Todo lo que impacta en sistema
        #validar
        formulario_contacto = contactForm(request.POST)
        if formulario_contacto.is_valid():
            # Validación personalizada: Comprobar la edad
            edad = formulario_contacto.cleaned_data.get('edad')
            if edad is not None and edad < 18:
                messages.error(request, 'Debes tener al menos 18 años para enviar el mensaje.')
            else:
                # Procesar el formulario si la edad es válida
                messages.success(request, 'Gracias! Hemos recibido sus datos. Muy pronto nos pondremos en contacto con usted')
                # Procesa los datos muestra mensaje de agradecimiento
                return redirect('Contacto')  
    else:
        return HttpResponseBadRequest('No es una respuesta valida')
    
    contexto = {
        'ahora': datetime.now,
        'formulario_contacto': formulario_contacto 
    }

    
    
    return render(request, "contacto.html", contexto)
 
 
def base(request):
    return render(request, "base.html")


def precios(request):
    return render(request, "precios.html")