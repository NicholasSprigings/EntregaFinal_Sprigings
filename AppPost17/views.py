from django.http import HttpResponse
from django.shortcuts import render
from .models import Portafolio

# Create your views here.

def portafolio(req, cliente, agencia):

    portafolio = Portafolio(cliente=cliente, agencia=agencia)
    portafolio.save()

    return HttpResponse(f"""
    <p>Cliente: {portafolio.cliente} - Agencia: {portafolio.agencia} creado con éxito!</p>
    """)   

def inicio(req):

    return render(req, "inicio.html")

def portafolio(req):

    return render(req, "portafolio.html")

def servicios(req):

    return render(req, "servicios.html")

def quienes_somos(req):

    return render(req, "quienes_somos.html")