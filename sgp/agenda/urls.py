from django.urls import path
from . import views

app_name = 'agenda'

urlpatterns = [
    path('mostrar/', views.mostrar, name="mostrar"),
]