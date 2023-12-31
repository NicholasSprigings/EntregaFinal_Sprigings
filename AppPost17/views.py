from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Portafolio
from .forms import FormularioContactanos, UserEditForm, PortafolioForm

# Create your views here.

# def portafolio(req, cliente, agencia):

    # portafolio = Portafolio(cliente=cliente, agencia=agencia)
    # portafolio.save()

    # return HttpResponse(f"""
    # <p>Cliente: {portafolio.cliente} - Agencia: {portafolio.agencia} creado con éxito!</p>
    # """)   

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

@login_required
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

def eliminar_usuario(req, id):

    if req.method == 'POST':

        usuario = usuario.objects.get(id=id)
        usuario.delete()

        usuario = usuario.objects.all()

        return render(req, "login.html", {"usuario": usuario, "id": usuario.id})

@login_required
def portafolio_list(request):
    portafolios = Portafolio.objects.all()
    return render(request, 'list.html', {'portafolios': portafolios})

@login_required
def portafolio_create(request):
    if request.method == 'POST':
        form = PortafolioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portafolio_list')  # Redirecciona a la lista de portafolios después de crear uno nuevo
    else:
        form = PortafolioForm()
    return render(request, 'form.html', {'form': form})

@login_required
def portafolio_update(request, pk):
    portafolio = Portafolio.objects.get(pk=pk)
    if request.method == 'POST':
        form = PortafolioForm(request.POST, instance=portafolio)
        if form.is_valid():
            form.save()
            return redirect('portafolio_list')  # Redirecciona a la lista de portafolios después de actualizar
    else:
        form = PortafolioForm(instance=portafolio)
    return render(request, 'form.html', {'form': form})

@login_required
def portafolio_delete(request, pk):
    portafolio = Portafolio.objects.get(pk=pk)
    if request.method == 'POST':
        portafolio.delete()
        return redirect('portafolio_list')  # Redirecciona a la lista de portafolios después de eliminar
    return render(request, 'delete.html', {'portafolio': portafolio})