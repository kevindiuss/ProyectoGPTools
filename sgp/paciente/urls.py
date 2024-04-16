from django.urls import path
from . import views

app_name = 'paciente'

urlpatterns = [
    path('listar/', views.listar, name="listar"),
    path('paciente_registro/', views.paciente_registro, name="paciente_registro"),
    path('editar/<cedula>/', views.editar, name="editar"),
    path('buscar/<cedula>/', views.buscar, name="buscar"),
    path('historia_clinica/<cedula>/', views.historia_clinica, name="historia_clinica"),
]