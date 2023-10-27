from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Contactanos, Portafolio 

# class FormularioContactanos(forms.Form):

    # nombre = forms.CharField(max_length=40)
    # apellido = forms.CharField(max_length=40)
    # email= forms.EmailField()
    # celular= forms.IntegerField()
    # mensaje = forms.CharField(max_length=1000)

class FormularioContactanos(forms.ModelForm):
    class Meta:
        model = Contactanos
        fields = ['nombre', 'apellido', 'email', 'celular', 'mensaje']

class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields = ("email", "first_name", "last_name", "password1", "password2")

    def clean_password2(self):

        print(self.cleaned_data)

        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden!!!!")
        return password2

class PortafolioForm(forms.ModelForm):
    class Meta:
        model = Portafolio
        fields = ['cliente', 'agencia']



