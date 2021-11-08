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
    return render(request,'home.html',context)

class GrupoDetailView(DetailView):
    model = Grupo
    context_object_name= 'grupoespecifico'
    template_name= 'grupo.html'

    def get_context_data(self, **kwargs):
        # Cargar el contexto base
        context = super().get_context_data(**kwargs)
        # Añadir un listado de departamentos
        context['editorial'] = Grupo.objects.all()
        return context

class GrupoListView(ListView):
    model = Grupo
    queryset = Grupo.objects.all()
    context_object_name= 'editorial'
    template_name= 'grupo_list.html'

class SuperheroesDetailView(DetailView):
    model = Superheroe

class SuperheroesListView(ListView):
    model = Superheroe
    template_name = 'superheroes_list.html'
    queryset = Superheroe.objects.all()
    context_object_name = 'superheroes'
	
    def get_context_data(self, **kwargs):
        # Cargar el contexto base
        context = super().get_context_data(**kwargs)
        # Añadir un listado de departamentos
        context['editorial'] = Grupo.objects.all()
        return context
        
class SuperpoderDetailView(DetailView):
    model = Superpoder

class SuperpoderListView(ListView):
    model = Superpoder
    template_name = 'superpoder_list.html'
    queryset = Superpoder.objects.all() #La info que mandamos al html
    context_object_name = 'superpoderes'  #cambio de nombre al objeto
    
    def get_context_data(self, **kwargs):
        context = super(SuperpoderListView, self).get_context_data(**kwargs)
        #context['superpoderes'] = Superpoder.objects.all()
        context['editorial'] = Grupo.objects.all()
        return context
	