from django.shortcuts import render, redirect
from datetime import datetime

from django.http import HttpResponse
from django.template import Template, Context, loader

from inicio.models import Vuelo

# Create your views here.
def inicio(request):
    return render(request, 'inicio/index.html')

def crear_vuelo(request, nombrevuelo, aerolinea, fabricante, modelo, pasajeros):
    vuelo= Vuelo(nombrevuelo=nombrevuelo, aerolinea=aerolinea, fabricante=fabricante, modelo=modelo, pasajeros=pasajeros)
    vuelo.save()
    return render(request, 'vuelo_template/creacion.html', {'vuelo': vuelo})