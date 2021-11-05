from django.http import request
from django.urls import path


from . import views


urlpatterns = [
    
    # ej: /miApp/
    path('', views.index, name='index'),
]

