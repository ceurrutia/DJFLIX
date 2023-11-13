# En tu aplicación, crea un archivo context_processors.py
from django.contrib.auth.models import Group

def grupos_del_usuario(request):
    grupos = []
    if request.user.is_authenticated:
        grupos = request.user.groups.all()
    return {'grupos_del_usuario': grupos}
