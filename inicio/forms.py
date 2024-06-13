from django import forms

class CrearVueloFormulario(forms.Form):
    vuelo= forms.CharField(max_length=20)
    aerolinea= forms.CharField(max_length=30)
    fabricante= forms.CharField(max_length=20)
    modelo= forms.CharField(max_length=20)
    pasajeros= forms.IntegerField()