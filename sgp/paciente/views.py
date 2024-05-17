from django.shortcuts import render, redirect, Http404, get_object_or_404,get_list_or_404
from django.contrib.auth.decorators import login_required
from .models import Paciente
from django.core.paginator import Paginator
from .forms import PacienteForm
from vacunas.models import VacunasPacientes
from django.contrib import messages
from datetime import datetime

# Create your views here.

@login_required()
def listar(request):
    pacientes = Paciente.objects.all().order_by('-created')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(pacientes, 5)
        pacientes = paginator.page(page)
    except:
        raise Http404
    data = {
        'pacientes': pacientes,
        'paginator': paginator
    }
    return render(request, 'paciente/listar.html', data)

@login_required()
def paciente_registro(request):
    data = {
        'form': PacienteForm
    }
    if request.method == 'POST':
        print("hola men1")
        formulario = PacienteForm(data=request.POST)
        if formulario.is_valid():
            print("hola men2")
            formulario.save()
            # solicitar id de paciente en "PacienteForm" en incluirlo en tabla "vacunasPacientes"


            messages.success(request, "Paciente registrado correctamente.")
            return redirect(to="/listar")
        data["form"] = formulario
    return render(request, 'paciente/paciente_registro.html',data)

@login_required()
def editar(request, cedula):
    paciente = get_object_or_404(Paciente, cedula=cedula)
    data = {
        'form': PacienteForm(instance=paciente)
    }
    if request.method == "POST":
        formulario = PacienteForm(data=request.POST, instance=paciente)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Datos del paciente actualizados!")
            return redirect(to='/listar')
        data["form"] = formulario
    return render(request, 'paciente/editar.html', data)

@login_required()
def buscar(request, cedula):    
    try:
        paciente = get_list_or_404(Paciente, numDocumento=cedula)
        print(paciente)
        print(paciente[0])
        edad = Paciente.calcularEdad(paciente[0])
        data = {
            'paciente': paciente[0],
            'edad': edad
        }
        return render(request, 'paciente/buscar.html', data)
    except:
        messages.success(request, "No existe paciente con ese Numero de Documento.")
        return redirect(to="/listar")

@login_required()
def historia_clinica(request, cedula):
    try:
        paciente = get_object_or_404(Paciente, cedula=cedula)
        data = {
            'paciente': paciente
        }
        return render(request, 'paciente/historia_clinica.html', data)
    except:
        messages.success(request, "No existe historia clínica para el paciente.")
        return redirect(to="/listar")