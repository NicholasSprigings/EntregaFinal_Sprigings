from django import forms

class FormularioContactanos(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email= forms.EmailField()
    celular= forms.IntegerField()
    mensaje = forms.CharField(max_length=1000)