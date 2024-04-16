from django.urls import path
from . import views

app_name = 'tratamiento'

urlpatterns = [
    path('listar_tratamientos/', views.listar_tratamientos, name="listar_tratamientos"),
    path('ver_tratamiento/<id>', views.ver_tratamiento, name="ver_tratamiento"),
    path('paciente_tratamientos/<id>', views.paciente_tratamientos, name="paciente_tratamientos"),
    path('paciente_radiografias/<id>', views.paciente_radiografias, name="paciente_radiografias"),
    path('registrar_tratamiento', views.registrar_tratamiento, name="registrar_tratamiento"),
    path('guardar_radiografia_tratamiento', views.guardar_radiografia_tratamiento, name="guardar_radiografia_tratamiento"),
]