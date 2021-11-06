from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Grupo, Superheroe, Superpoder 
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.
def index(request):
    grupos = Grupo.objects.all()
    context= {
        'editorial':grupos
    }
    return render(request,'index.html',context)

class GrupoDetailView(DetailView):
    model = Grupo
class GrupoListView(ListView):
    model = Grupo
    queryset = Grupo.objects.all()
class SuperheroesDetailView(DetailView):
    model = Superheroe

class SuperpoderDetailView(ListView):
    model = Superpoder
