from django.http import request
from django.urls import path

from heroWeb.models import Superpoder
from .views import GrupoDetailView, SuperheroesDetailView, SuperpoderDetailView


from . import views


urlpatterns = [
    
    # ej: /heroWeb/
    path('', views.index, name='index'),

    #/heroWeb/grupos
    path('<str:nombre>/', GrupoDetailView.as_view(), name='grupos'),
    #/heroApp/grupos/[id_Superheroe] --> Por si hay dos superheroes con nombres iguales
    path('grupos/<int:id>/', SuperheroesDetailView.as_view(), name='superheroes'),
    #/heroApp/superehores/[nombre_Habilidad] 
    path('superheroes/<str:nombre_superpoder>/', SuperpoderDetailView.as_view(), name='superpoderes')

]

