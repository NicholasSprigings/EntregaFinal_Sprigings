from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('agrega-portafolio/<cliente>/<agencia>', portafolio),
    path('', inicio, name="Inicio"),
    path('portafolio/', portafolio, name="Portafolio"),
    path('servicios/', servicios, name="Servicios"),
    path('quienes_somos/', quienes_somos, name="Quienes Somos"),
    path('formulariocontactanos /', formulario_contactanos, name="formulario_contactanos"),
    path('login/', loginView, name="Login"),
    path('register/', register, name="Registrar"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path('editarPerfil/', editar_perfil, name="EditarPerfil"),
    path('eliminarusuario/<int:id>', eliminar_usuario, name="EliminarUsuario"),
    path('portafolio/', portafolio_list, name='portafolio_list'),
    path('portafolio/list/', portafolio_list, name='portafolio_list'),
    path('portafolio/crear/', portafolio_create, name='portafolio_create'),
    path('portafolio/editar/<int:pk>/', portafolio_update, name='portafolio_update'),
    path('portafolio/eliminar/<int:pk>/', portafolio_delete, name='portafolio_delete'),
]