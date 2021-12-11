from django.http import request
from django.urls import path

from heroWeb.models import Superpoder
from .views import ajax, GrupoDetailView, SuperheroesDetailView, SuperpoderDetailView,GrupoListView,SuperheroesListView,SuperpoderListView


from . import views


urlpatterns = [
    
    # ej: /heroWeb/
    path('', views.index, name='index'),
    path('grupos/<int:pk>/', GrupoDetailView.as_view(), name='grupo'), #Grupo especifico
    path('grupos/', GrupoListView.as_view(), name='grupos'), #Lista de grupos
    path('superheroes/', SuperheroesListView.as_view(), name='superheroes'),#Lista de superheroes 
    path('superheroesAjax/<int:pk>/', ajax.as_view(), name='ajax'), #URL para pop up Ajax
    path('superheroes/<int:pk>/', SuperheroesDetailView.as_view(), name='superheroe'), #Un heroe especifico 
    path('superpoderes/<int:pk>/', SuperpoderDetailView.as_view(), name='ssuperpodere'), #Un superpoder especifico
    path('superpoderes/', SuperpoderListView.as_view(), name='superpoderes'), #Lista superpoderes 
    
]

