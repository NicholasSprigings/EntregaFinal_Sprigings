from django.urls import path
from .views import *

urlpatterns = [
    path('agrega-portafolio/<cliente>/<agencia>', portafolio),
     path('', inicio, name="Inicio"),
    path('portafolio/', portafolio, name="Portafolio"),
    path('servicios/', servicios, name="Servicios"),
    path('quienes_somos/', quienes_somos, name="Quienes Somos"),
    path('formulariocontactanos /', FormularioContactanos, name="FormularioContactanos"),
]