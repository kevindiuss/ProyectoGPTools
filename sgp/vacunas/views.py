from paciente.models import Paciente
from django.shortcuts import render, redirect, Http404, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import VacunasPacientes
from django.contrib import messages
from vacunas.models import VacunasPacientes

from vacunas.models import NEUMOCON
from vacunas.forms import NEUMOCOCO


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

        match bio:
            case "1000":
                print("Unica")

            case "1001":
                print("1ra dosis")

            case "1002":
                print("2da dosis")

            case "1003":

                vacunaregistrar="NEUMOCOCO_CONJUGADO"

            case "1004":
                print("4ta dosis")

            case "1005":
                print("5ta dosis")

            case "1006":
                print("6ta dosis")

            case "1007":
                print("7ma dosis")

        formulario = NEUMOCOCO(data=request.POST, files=request.FILES)
        print(request.POST)
        if formulario.is_valid():
            #Completo el paciente
            formulario.instance.PACIENTE = get_object_or_404(Paciente, id=request.POST['PACIENTE'])
            formulario.save()
            messages.success(request, "Se guardaron los datos del tratamiento.")
            return redirect(to="/listar_tratamientos")


        # Marca la vacuna como aplicada en esquema

        holawey=VacunasPacientes

        esquemapaciente=holawey.objects.get(PACIENTE_id=id)

        esquemapaciente.__setattr__(vacunaregistrar,"hola")
        esquemapaciente.save()

        # prueba esto es para neumococo
        # lainstancia=Paciente.objects.get(id=id)
        # formNeumocon= NEUMOCOCO(data=request.POST)

        # neumovacuna=NEUMOCON(PACIENTE=lainstancia,formNeumocon)


        messages.success(request, "Biológico cargado correctamente.")

        # Devuelve pagina esquema de paciente
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

            vacunaregistrar="NEUMOCOCO_CONJUGADO"

            PacienteActual=Paciente.objects.get(id=id)

            data={
                'biologico':'Neumococo Conjugado',
                'dosis':'3ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'idpaciente':PacienteActual.pk,
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
