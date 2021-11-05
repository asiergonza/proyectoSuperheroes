from django.http import request
from django.urls import path
from .views import GrupoDetailView


from . import views


urlpatterns = [
    
    # ej: /heroWeb/
    path('', views.index, name='index'),

    #/heroWeb/grupos
    path('<str:nombre>/', GrupoDetailView.as_view(), name='grupos'),
    #/heroApp/grupos/[id_Superheroe] --> Por si hay dos superheroes con nombres iguales
    #path('grupos/<int:pk>', SupereroesDetailView.as_view(), name='superheroes'),
    #/heroApp/superehores/[nombre_Habilidad] 
    #path('superheroes/<str:nombre_superpoder>', SuperpoderesDetailView.as_view(), name='superpoderes')

]

