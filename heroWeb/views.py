from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Grupo, Superheroe, Superpoder 
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_list_or_404

# Create your views here.
def index(request):
    grupos = get_list_or_404(Grupo)
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
class SuperheroesListView(ListView):
    model = Superheroe
    queryset = Superheroe.objects.all()
class SuperpoderDetailView(DetailView):
    model = Superpoder
class SuperpoderListView(ListView):
    model = Superpoder
    queryset = Superpoder.objects.all()