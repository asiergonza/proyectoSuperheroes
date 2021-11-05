from django.http import request
from django.urls import path


from . import views


urlpatterns = [
    
    # ej: /heroApp/
    path('', views.index, name='index'),

    #/heroApp/grupos
    #path('grupos', noseque.as_view(), name='grupos'),
    #/heroApp/grupos/[id_Superheroe] --> Por si hay dos superheroes con nombres iguales
    #path('grupos/<int:pk>', noseque2.as_view(), name='superheroes'),
    #/heroApp/superehores/[nombre_Habilidad] 
    #path('superheroes/<str:nombre_superpoder>', noseque3.as_view(), name='superpoderes')

]

