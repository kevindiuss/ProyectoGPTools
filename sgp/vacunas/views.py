from paciente.models import Paciente
from django.shortcuts import render, redirect, Http404, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import VacunasPacientes
from django.contrib import messages


# Create your views here.

def vacunas(request, cedula):

    paciente = get_list_or_404(Paciente, numDocumento=cedula)
    print(paciente)
    print(paciente[0])
    edad = Paciente.calcularEdad(paciente[0])
    data = {
        'paciente': paciente[0],
        'edad': edad
    }
    return render(request, 'vacunas/lista_vacunas.html', data)
    
def infova(request, id, bio):

    if request.method == 'POST':
        print("hola men1")

        messages.success(request, "Biológico cargado correctamente.")

        PacienteActual=Paciente.objects.get(id=id)

        numDocPaciente=PacienteActual.numDocumento

        return redirect('/biologicos/'+numDocPaciente)
    

    match bio:
        case "1000":
            print("Unica")

        case "1001":
            print("1ra dosis")

        case "1002":
            print("2da dosis")

        case "1003":
            PacienteActual=Paciente.objects.get(id=id)

            data={
                'biologico':'Neumococo Conjugado',
                'dosis':'3ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido
            }

            print(PacienteActual, "hola people")

            return render(request, 'vacunas/info_vacunas.html', data)

        case "1004":
            print("4ta dosis")

        case "1005":
            print("5ta dosis")

        case "1006":
            print("6ta dosis")

        case "1007":
            print("7ma dosis")

    
    return render(request, 'vacunas/info_vacunas.html')
