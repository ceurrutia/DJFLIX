from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_djlix import views

mi_router = DefaultRouter()
mi_router.register('peliculas',views.PeliculaViewSet, basename= 'peliculas')


urlpatterns = [
    path('', include(mi_router.urls)),
    path('api_auth', include ('rest_framework.urls', namespace='rest_framework'))
]
