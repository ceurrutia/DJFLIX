from django.urls import path, include
from administracion import views

urlpatterns = [
    
    path('administracion/', views.administracion, name="administracion"),
    path('base_admin/', views.base_admin, name = "base_admin"),
    path('listado_peliculas/', views.listado_peliculas, name='listado_peliculas'),
    path('create_pelicula/', views.pelicula_crear, name = "create_pelicula"),
    path('pelicula/<int:pk>/editar/', views.pelicula_editar, name='pelicula_editar'),
    path('pelicula/<int:pk>/eliminar/', views.pelicula_eliminar, name='pelicula_eliminar'),
    path('create_categorias/', views.create_categoria, name = "create_categoria"),
    path('listado_categorias/', views.listado_categorias, name = "listado_categorias"),
    path('serie_lista/', views.serie_lista, name='serie_lista'),
    path('serie_crear/', views.serie_crear, name='serie_crear'),
    path('serie/<int:pk>/editar/', views.serie_editar, name='serie_editar'),
    path('serie/<int:pk>/eliminar/', views.serie_eliminar, name='serie_eliminar'),
    path('listado_suscriptores/', views.listado_suscriptores, name = "listado_suscriptores"),
    path('alta_suscriptor/', views.create_suscriptor, name = "alta_suscriptor"),
    path('suscriptor/<int:pk>/editar/', views.suscriptor_editar, name='suscriptor_editar'),
    path('suscriptor/<int:pk>/eliminar/', views.suscriptor_eliminar, name='suscriptor_eliminar'),
   
]
