from django.contrib import admin

from .models import Superheroe,Grupo, Superpoder
# Register your models here.
admin.site.register(Grupo)
admin.site.register(Superheroe)
admin.site.register(Superpoder)
