from django.shortcuts import render, redirect, Http404, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from paciente.models import Paciente
from django.contrib import messages


# Create your views here.

def vacunas(request):
    

    return render(request, 'vacunas/lista_vacunas.html')

