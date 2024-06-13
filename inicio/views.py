from django.shortcuts import render, redirect
from datetime import datetime

from django.http import HttpResponse
from django.template import Template, Context, loader

from inicio.models import Vuelo
from inicio.forms import CrearVueloFormulario

# Create your views here.
def inicio(request):
    return render(request, 'inicio/index.html')

def crear_vuelo_v1(request, nombrevuelo, aerolinea, fabricante, modelo, pasajeros):
    vuelo= Vuelo(nombrevuelo=nombrevuelo, aerolinea=aerolinea, fabricante=fabricante, modelo=modelo, pasajeros=pasajeros)
    vuelo.save()
    return render(request, 'inicio/crear_vuelo.html', {'vuelo': vuelo})

def crear_vuelo(request):
    formulario = CrearVueloFormulario()
    if request.method == 'POST':
        formulario = CrearVueloFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            vuelo = Vuelo(
                vuelo=datos.get('vuelo'),
                aerolinea=datos.get('aerolinea'),
                fabricante=datos.get('fabricante'),
                modelo=datos.get('modelo'),
                pasajeros=datos.get('pasajeros')
            )
            vuelo.save()
            return redirect('listado')
    
    return render(request, 'inicio/crear_vuelo.html', {'formulario': formulario})

def listado(request):
    
    vuelos = Vuelo.objects.all()
    
    return render(request, 'inicio/listado.html', {'vuelos': vuelos})