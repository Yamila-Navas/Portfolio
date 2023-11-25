from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UsuarioManage(BaseUserManager):
    def create_user(self,nombre,apellido,email,contraseña=None, **extras_field):
        if not email:
            raise ValueError('El campo email es obligatorio')
        
        email = self.normalize_email(email)

        # creo una instancia del usuario:
        usuario = self.model(nombre=nombre,
                             apellido=apellido,
                             email=email,
                             **extras_field)
        
        # establezco de manera segura la contraseña del usuario:
        usuario.set_password(contraseña)

        # guardo al usuario en la db:
        usuario.save()
        
        return usuario


class Usuarios(AbstractBaseUser):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    solicitud = models.BooleanField(default=False)

    # contraseña y el manager personalizado:
    contraseña = models.CharField(max_length=8)
    objects= UsuarioManage()

    # el campo de email se utilizará como el nombre de usuario para la autenticación:
    USERNAME_FIELD = 'email'

    # campos adicionales requeridos al crear un usuario:
    REQUIRED_FIELDS = ['nombre', 'apellido']

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    

class Motociclistas(models.Model):
    horario = models.TimeField()
    motociclistas = models.PositiveIntegerField(default=8)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f'hora: {self.horario} - motociclistas: {self.motociclistas} - estado: {self.estado}'