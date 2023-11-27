from django.urls import path
from . import views

app_name = 'motociclistas'
urlpatterns = [
    path('', views.index, name='index'),
    path('registrate/', views.registro_usuario, name='registro_usuario'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('sesion/', views.sesion, name='sesion' ),
    path('solicitud/<int:id>/', views.solicitud, name='solicitud'),
    path('liberar/<int:id>/', views.liberar, name='liberar'),
    path('cerrar_sesion', views.cerrar_sesion, name='cerrar_sesion'),
    path('restablecer/', views.restablecer, name='restablecer')
    
]
