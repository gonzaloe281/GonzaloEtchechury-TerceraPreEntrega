from django.db import models

# Create your models here.
class Vuelo(models.Model):
    nombrevuelo= models.CharField(max_length=20)
    aerolinea= models.CharField(max_length=30)
    fabricante= models.CharField(max_length=20)
    modelo= models.CharField(max_length=20)
    pasajeros= models.IntegerField()