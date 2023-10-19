from django.urls import path, include
from administracion import views

urlpatterns = [
    
    path('administracion/', views.administracion, name="administracion"),
    path('base_admin/', views.base_admin, name = "base_admin"),
    path('create_pelicula/', views.create_pelicula, name = "create_pelicula")
]
