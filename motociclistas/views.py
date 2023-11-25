from audioop import reverse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Motociclistas
from .forms import RegistroForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(req):
    horarios = Motociclistas.objects.all()

    context = {
        'horarios' : horarios 
    }

    return render(req, 'index.html', context)


def registro_usuario(req):
    if req.method == 'POST':
        form = RegistroForm(req.POST)
        if form.is_valid():
            usuario = form.save()
            #autenticacion de usuario:
            login(req, usuario)
            return JsonResponse({'success': True, 'message': 'Usuario registrado y autenticado correctamente.'})
        else:
            errors = form.errors
            return JsonResponse({'success': False, 'errors': errors})   
    else:
        form = RegistroForm()

    context = {
        'form' : form
    }
    return render(req, 'registro_usuario.html', context)


def iniciar_sesion(req):
    if req.method == 'POST':
        email = req.POST['email']
        contraseña = req.POST['contraseña']

        #autenticar al usuario:
        usuario = authenticate(req, email=email, password=contraseña)

        if usuario is not None:
            login(req, usuario)
            messages.success(req, 'Inicio de sesión exitoso.')
            
            
             # Redirigir a la URL de la vista 'sesion'
            return redirect(reverse_lazy('motociclistas:sesion'))
        else:
            messages.error(req, 'Credenciales incorrectas. Por favor, inténtalo de nuevo.')
     
    return render(req, 'iniciar_sesion.html')


@login_required
def sesion(req):
    horarios = Motociclistas.objects.all()

    nombre = req.user.nombre
    apellido = req.user.apellido


    context = {
        'horarios' : horarios,
        'nombre' : nombre,
        'apellido' : apellido
    }

    return render(req, 'sesion_usuario.html', context)


def cerrar_sesion(req):
    logout(req)
    return redirect('motociclistas:index')


'''@login_required
def solicitud(req, id):
    horario = Motociclistas.objects.get(id = id)

    if horario.motociclistas >= 1:
        horario.motociclistas = horario.motociclistas - 1'''





    
