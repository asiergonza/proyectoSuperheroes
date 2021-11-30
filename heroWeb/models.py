from django.db import models

# Create your models here.

class Grupo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=350)
    icono = models.URLField(max_length=300)
    marca = models.TextChoices('Marca', 'DC MARVEL OTROS')
    def __str__(self) -> str:
        return f"{self.nombre}"

class Superheroe(models.Model):
 # Campo para la relación
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=70)
    icono = models.URLField(max_length=300)
    fecha_nacimiento = models.DateField()
    muerto = models.BooleanField()
    id_api = models.CharField(max_length=20, blank=True)
    def __str__(self) -> str:
        return f"{self.nombre}"

class Superpoder(models.Model):
    superheroe = models.ManyToManyField(Superheroe)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=350)
    def __str__(self) -> str:
        return f"{self.nombre}"
