from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    # path('vuelos/crear/<str:nombrevuelo>/<str:aerolinea>/<str:fabricante>/<str:modelo>/<int:pasajeros>', views.crear_vuelo, name='crear_vuelo'),
    path('vuelos/', views.listado, name='listado'),
    path('vuelos/crear/', views.crear_vuelo, name='crear_vuelo'),
    
    
]
