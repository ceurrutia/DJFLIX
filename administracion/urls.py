from django.urls import path, include
from administracion import views

urlpatterns = [
    
    #path('administracion/', views.administracion, name="administracion"),
    path('administracion/', views.PeliculasListView.as_view(), name='administracion'),
    path('base_admin/', views.base_admin, name = "base_admin"),
    path('create_pelicula/', views.create_pelicula, name = "create_pelicula"),
    path('create_categorias/', views.create_categoria, name = "create_categoria"),
    #path('editar_categoria/<int:categoria_id>/', views.edit_categoria, name='editar_categoria'),
    path('listado_categorias/', views.listado_categorias, name = "listado_categorias"),
    path('listado_suscriptores/', views.listado_suscriptores, name = "listado_suscriptores"),
    path('alta_suscriptor/', views.create_suscriptor, name = "alta_suscriptor"),
   
]
