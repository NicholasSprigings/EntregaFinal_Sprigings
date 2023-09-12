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
