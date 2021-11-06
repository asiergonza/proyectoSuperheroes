from django.http import request
from django.urls import path

from heroWeb.models import Superpoder
from .views import GrupoDetailView, SuperheroesDetailView, SuperpoderDetailView


from . import views


urlpatterns = [
    
    # ej: /heroWeb/
    path('', views.index, name='index'),

    #/heroWeb/grupos lista de grupos
    path('<str:nombre>/', GrupoDetailView.as_view(), name='grupos'),

    #/heroApp/grupos/[id_Superheroe] --> Por si hay dos superheroes con nombres iguales
    path('grupos/<int:id>/', SuperheroesDetailView.as_view(), name='superheroes'),
    #/heroApp/superehores/[nombre_Habilidad] 
    path('superheroes/<str:nombre_superpoder>/', SuperpoderDetailView.as_view(), name='superpoderes')
    #Propuesta Guiller
    #path('', views.index, name='index'), #pagina oficial
    #path('grupos/', GrupoListView.as_view(), name='grupos'), #lista de grupos
    #path('grupos/<int:id>/', GrupoDetailView.as_view(), name='grupo'), #Grupo especifico
    #path('superheroes/', SuperheroesListView.as_view(), name='superheroes'),#Lista de superheroes
    #path('superheroes/<int:id>/', SuperheroesDetailView.as_view(), name='superheroe'), #Un heroe especifico
    #path('superpoderes/', SuperpoderListView.as_view(), name='superpoderes'), #Lista superpoderes
    #path('superpoderes/<int:id>/', SuperpoderDetailView.as_view(), name='superpodere'), #Un superpoder especifico
]

