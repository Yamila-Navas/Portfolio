from django.http import  JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
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
            return redirect(reverse_lazy('motociclistas:iniciar_sesion'))
        else:
            return render(req, 'registro_usuario.html', context)  
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
    id_usuario = req.user.id


    context = {
        'horarios' : horarios,
        'nombre' : nombre,
        'apellido' : apellido, 
        'id_usuario' : id_usuario
    }

    return render(req, 'sesion_usuario.html', context)


def cerrar_sesion(req):
    logout(req)
    return redirect('motociclistas:index')


@login_required
def solicitud(req, id):
    horario = get_object_or_404(Motociclistas, id=id)

    if horario.motociclistas >= 1:
        horario.motociclistas = horario.motociclistas - 1
        horario.save()
        nuevo_valor =  horario.motociclistas 

        return JsonResponse({'success': True, 'message': 'Accion exitosa', 'nuevo_valor':horario.motociclistas })       

    return JsonResponse({'success': False, 'message': 'No hay motociclistas disponibles en este horario.'})


@login_required
def liberar(req, id):
    horario = get_object_or_404(Motociclistas, id=id)

    if horario.motociclistas <= 7:
        horario.motociclistas = horario.motociclistas + 1
        horario.save()
        

        return JsonResponse({'success': True, 'message': 'Accion exitosa', 'nuevo_valor':horario.motociclistas })

    return JsonResponse({'success': False, 'message': 'Ocurrio un error'})


def restablecer(req):
    horarios = Motociclistas.objects.all()
    for horario in horarios:
        horario.motociclistas = 8
        horario.save()
    
    return JsonResponse({'success': True, 'massege': 'valores restablecidos'})




    
