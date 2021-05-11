from django.db import models
from django.urls import reverse

# Create your models here.
class Lenguajes(models.Model):
    nombre = models.CharField(max_length=50)

class Modelo(models.Model):
    nombre = models.CharField(max_length=80)
    foto = models.TextField()
    educacion = models.CharField(max_length=100)
    experiencia = models.TextField()
    lenguajes = models.ForeignKey(
        Lenguajes,
        null=True,
        blank=True,
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return self.nombre

def get_absolute_url(self):
        return reverse('modelos', args=[str(self.id)])
