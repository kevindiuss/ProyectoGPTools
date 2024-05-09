from django.urls import path
from . import views

app_name = 'biologicos'

urlpatterns = [
    path('biologicos/', views.vacunas, name="vacunas"),

]