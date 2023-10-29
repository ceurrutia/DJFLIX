from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError, HttpResponseBadRequest
from django.urls import reverse
from django.shortcuts import render, redirect
#from django.template import loader
from datetime import datetime
from django.template import Template
from portal.forms import contactForm
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from .models import Contacto

TIPO_CONSULTA = (
    ('', '-Seleccione-'),
    (1, 'Soporte'),
    (2, 'Consultas sobre peliculas o series'),
    (3, 'Trabajar en DJflix'),
)


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
            nombreApellido= formulario_contacto.cleaned_data.get('nombreApellido')
            mail = formulario_contacto.cleaned_data.get('mail')
            telefono = formulario_contacto.cleaned_data.get('telefono')
            tipoconsulta = int(formulario_contacto.cleaned_data.get('tipo_consulta'))
            for tupla in TIPO_CONSULTA:
                if tupla[0]==tipoconsulta:
                    tipo_de_consulta=tupla[1]
            recibir_mail = formulario_contacto.cleaned_data.get('recibir_mail')
            mensaje = formulario_contacto.cleaned_data.get('mensaje')
            # Validación personalizada: Comprobar la edad
            edad = formulario_contacto.cleaned_data.get('edad')
            if edad is not None and edad < 18:
                messages.error(request, 'Debes tener al menos 18 años para enviar el mensaje.')
            else:
                # Procesar el formulario si la edad es válida
                messages.success(request, 'Gracias! Hemos recibido sus datos. Muy pronto nos pondremos en contacto con usted')
                #De acuerdo a checkbox, envia email con datos de formulario de contacto
                if recibir_mail==True:
                    send_mail(
                        'Confirmacion de contacto con Djflix',
                        f'''Gracias! Hemos recibido su mensaje. Muy pronto nos pondremos en contacto con usted 
                        \nNombre y apellido:{nombreApellido}  \nEmail: {mail} \nEdad:{edad} \nTelefono:{telefono}\nTipo_consulta:{tipo_de_consulta} \nMensaje:{mensaje}''' ,
                        'djflix.contacto@gmail.com',  # Remitente
                        [mail],  # Lista de destinatarios
                        fail_silently=False,  # Cambia a True para manejar errores silenciosamente
                    )
                c1= Contacto(
                    nombre_y_apellido = formulario_contacto.cleaned_data.get('nombreApellido'),
                    edad= formulario_contacto.cleaned_data.get('edad'),
                    telefono= formulario_contacto.cleaned_data.get('telefono'),
                    email=formulario_contacto.cleaned_data.get('mail'),
                    tipo_de_consulta= formulario_contacto.cleaned_data.get('tipo_consulta'),
                    mensaje = formulario_contacto.cleaned_data.get('mensaje'),
                    se_envio_email= formulario_contacto.cleaned_data.get('recibir_mail')
                )
                c1.save()

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