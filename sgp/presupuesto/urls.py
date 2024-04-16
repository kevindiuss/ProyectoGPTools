from django.urls import path
from . import views

app_name = 'presupuesto'

urlpatterns = [
    path('listar_presupuestos/', views.listar_presupuestos, name="listar_presupuestos"),
]