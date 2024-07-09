from django.urls import path
from . import views

app_name = 'biologicos'

urlpatterns = [
    path('biologicos/<cedula>/', views.vacunas, name="vacunas"),
    path('infovacuna/<id>/<bio>/',views.infova, name='informacionva')

]