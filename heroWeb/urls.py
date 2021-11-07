from django.http import request
from django.urls import path

from heroWeb.models import Superpoder
from .views import GrupoDetailView, SuperheroesDetailView, SuperpoderDetailView,GrupoListView,SuperheroesListView,SuperpoderListView


from . import views


urlpatterns = [
    
    # ej: /heroWeb/
    path('', views.index, name='index'),
    path('grupos/', GrupoListView.as_view(), name='grupos'), #lista de grupos
    path('grupos/<str:nombre>/', GrupoDetailView.as_view(), name='grupo'), #Grupo especifico
    path('superheroes/', SuperheroesListView.as_view(), name='superheroes'),#Lista de superheroes
    path('superheroes/<int:id>/', SuperheroesDetailView.as_view(), name='superheroe'), #Un heroe especifico
    path('superpoderes/', SuperpoderListView.as_view(), name='superpoderes'), #Lista superpoderes
    path('superpoderes/<int:id>/', SuperpoderDetailView.as_view(), name='superpodere'), #Un superpoder especifico
]

