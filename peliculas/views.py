from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse
from django.shortcuts import render
from datetime import datetime
from django.template import Template
from administracion.models import Pelicula
# Create your views here.


def peliculas(request):
    peliculas = Pelicula.objects.all()  # Obtiene todas las películas desde la base de datos
    context = {
        'peliculas': peliculas, 
        'es_suscriptor': True,
        'usuario_conectado': True,
        'nombre_usuario': 'Genérico',
    }
    return render(request, "peliculas.html", context)



def detallepelicula(request):
    return render(request, "detallepelicula.html")
    
    
def archivo(request, year):
    if year == 2028:
        url = reverse("index")
        return HttpResponseRedirect(url)
    elif year == 2027:
        return HttpResponseServerError("<h1> Error de servidor </h1>")
    
    return HttpResponse(f'<h1>Peliculas de archivo del anio: {year}</h1>')

    return response

def series(request):
    #return HttpResponse("<h1> Todas las peliculas </h1>" )
    #Contexto: el o  los datos que le damos a la plantilla para que se cargue
    context = {
        'titulo': '',
        'imagen': '',
        'listado_series':[ 
            {'nombre':'Friends'  ,'anio':'1994','categoria': 'Sitcom' ,'imagen': 'friends.jpg' ,'descripcion':'Sigue las aventuras y desventuras en el trabajo, el amor y la vida de seis amigos veinteañeros que viven en Manhattan durante los noventa',
                 "capitulos":[{'nombre':'Monica tiene compañera', 'duracion':'25','imagen': 'friends1.jpg'},{'nombre':'Ecografia al final','duracion':'24','imagen': 'friends1.jpg'},{'nombre':'El del pulgar','duracion':'24','imagen': 'friends1.jpg'},{'nombre':'El de George Stephanopoulos','duracion':'24','imagen': 'friends1.jpg'}]},
            {'nombre':'The Nanny','anio':'1993','categoria': 'Sitcom','imagen': 'thenanny.jpg','descripcion':'Protagonizada por Fran Drescher, quien interpretó a Fran Fine, que por accidente se convierte en la niñera de tres niños de clase alta de Nueva York.',
                 "capitulos":[{'nombre':'Piloto', 'duracion':'25','imagen': 'thenanny1.jpg'},{'nombre':'Smoke Gets in Your Lies','duracion':'24','imagen': 'thenanny1.jpg'}]},
            {'nombre':'Peaky Blinders'  ,'anio':'2022','categoria': 'Drama' ,'imagen': 'peakyblinders.jpg' ,'descripcion':'Peaky Blinders es una serie de televisión inglesa de drama histórico, emitida por el canal BBC Two. La serie está protagonizada por Cillian Murphy y se centra en una familia de gánsteres de Birmingham, durante los años veinte y del ascenso de su jefe, Thomas Shelby.',
                 "capitulos":[{'nombre':'The Noose', 'duracion':'54','imagen': 'peakyblinders1.jpg'},{'nombre':'Heathens','duracion':'42','imagen': 'peakyblinders1.jpg'},{'nombre':'Blackbird','duracion':'39','imagen': 'peakyblinders1.jpg'}]}
        ],
        'ahora': datetime.now(),
        'es_suscriptor': True,
        'usuario_conectado': True,
        'nombre_usuario': 'Juan Perez'
    }
    
    return render(request, "series.html", context)
