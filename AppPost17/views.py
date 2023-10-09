from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Portafolio
from .forms import FormularioContactanos, UserEditForm

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

#def FormularioContactanos(req):

    #return render(req, "formulariocontactanos.html")

#def FormularioContactanos(request):

    print('method', request.method)
    print('POST', request.POST)

    if request.method == 'POST':

        form = FormularioContactanos(request.POST)

        if form.is_valid():

            data = FormularioContactanos.cleaned_data
            form = form(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], 
            celular=data["celular"], mensaje=data["mensaje"])
            form.save()
            
            return render(request, "inicio.html")
    
    else:

        form = FormularioContactanos(request)
        return render(request, 'formulariocontactanos.html', {'form': form})

def formulario_contactanos(request):
    if request.method == 'POST':
        form = FormularioContactanos(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            return render(request, "inicio.html")  # Redirect to another page on success
    else:
        form = FormularioContactanos()  # Create a new form for GET requests
    return render(request, 'formulariocontactanos.html', {'form': form})

def loginView(req):

    if req.method == 'POST':

        miFormulario = AuthenticationForm(req, data=req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)
            if user:
                login(req, user)
                return render(req, "inicio.html", {"mensaje": f"Bienvenido {usuario}!"})
            
        return render(req, "inicio.html", {"mensaje": f"Datos incorrectos"})
    else:
        miFormulario = AuthenticationForm()
        return render(req, "login.html", {"miFormulario": miFormulario})

def register(req):

    if req.method == 'POST':

        miFormulario = UserCreationForm(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            usuario = data["username"]
            miFormulario.save()
            return render(req, "inicio.html", {"mensaje": f"Usuario {usuario} creado con éxito!"})

        return render(req, "inicio.html", {"mensaje": f"Formulario invalido"})
            
    else:
        miFormulario = UserCreationForm()
        return render(req, "registro.html", {"miFormulario": miFormulario})

def editar_perfil(req):

    usuario = req.user
    if req.method == 'POST':

        miFormulario = UserEditForm(req.POST, instance=req.user)

        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])
            usuario.save()

            return render(req, "inicio.html", {"mensaje": "Datos actualizados con éxito!"})
        else:
            return render(req, "editarPerfil.html", {"miFormulario": miFormulario})

    else:
        miFormulario = UserEditForm(instance=usuario)
        return render(req, "editarPerfil.html", {"miFormulario": miFormulario})