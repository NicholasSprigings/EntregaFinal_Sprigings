from django.http import HttpResponse
from django.shortcuts import render
from .models import Portafolio
from .forms import FormularioContactanos

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

def FormularioContactanos(req):

    return render(req, "formulariocontactanos.html")


# def cursoFormulario(req):

    #print('method', req.method)
   # print('POST', req.POST)

   # if req.method == 'POST':

   #     Contactanos = FormularioContactanos(req.POST)

   #     if FormularioContactanos.is_valid():

   #         data = FormularioContactanos.cleaned_data
   #         curso = Nombre(nombre=data["curso"], camada=data["camada"])
   #         curso.save()

   #         return render(req, "inicio.html")
   # else:

   #     miFormulario = CursoFormulario()
  #      return render(req, "cursoFormulario.html", {"miFormulario": miFormulario})