from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Grupo, Superheroe, Superpoder 
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.
def index(request):
    return HttpResponse('Página inicial')

class GrupoDetailView(DetailView):
    model = Grupo
