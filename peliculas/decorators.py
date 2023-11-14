from functools import wraps
from django.http import HttpResponseForbidden

def group_required(group_name): 
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(name=group_name).exists() :
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("No tienes permisos para acceder a esta página.")

        return wrapped_view

    return decorator

def group_required_or_staff(group_name): #grupo o staff
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(name=group_name).exists() or request.user.is_staff :
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("No tienes permisos para acceder a esta página.")

        return wrapped_view

    return decorator