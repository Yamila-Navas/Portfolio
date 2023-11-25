from django.forms import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuarios

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuarios
        fields = ['nombre', 'apellido', 'email']