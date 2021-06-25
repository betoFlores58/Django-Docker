from django.db import models
from django.urls import reverse
from django.conf import settings

class Tienda(models.Model):
    articulo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=6,decimal_places=2)
    imagen = models.ImageField(null=True,blank=True)
    stock = models.BooleanField(default=True)

    def __str__(self):
        return self.articulo
    
def get_absolute_url(self):
        return reverse('articulos', args=[str(self.id)])
