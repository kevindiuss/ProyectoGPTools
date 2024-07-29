from paciente.models import Paciente
from django.shortcuts import render, redirect, Http404, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import VacunasPacientes
from django.contrib import messages
from vacunas.models import VacunasPacientes

from vacunas.models import NEUMOCON
from vacunas.forms import NEUMOCOCO
from json import dumps


# Create your views here.

def vacunas(request, cedula):

    paciente = get_list_or_404(Paciente, numDocumento=cedula)
    esquemavacpaciente=get_object_or_404(VacunasPacientes, pk=paciente[0].pk)


    edad = Paciente.calcularEdad(paciente[0])
    data = {
        'paciente': paciente[0],
        'edad': edad,   
        'neumotres':'neumomihermano    ',
        'neumococo': esquemavacpaciente.NEUMOCOCO_CONJUGADO_3,
        'influenza': esquemavacpaciente.INFLUENZA_3
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

                vacunaregistrar="NEUMOCOCO_CONJUGADO_3"

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
        print(request.user)
        print(formulario.errors)
        if formulario.is_valid():
            #Completo el paciente
            formulario.instance.PACIENTE = get_object_or_404(Paciente, id=id)
            nombreusuario=str(request.user)
            formulario.instance.NOMBREVACUNADOR=nombreusuario

            formulario.save()
          
            # return redirect(to="/listar_tratamientos")


            # Marca la vacuna como aplicada en esquema

            holawey=VacunasPacientes

            esquemapaciente=holawey.objects.get(PACIENTE_id=id)

            esquemapaciente.__setattr__(vacunaregistrar,"si")
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
        
        
        PacienteActual=Paciente.objects.get(id=id)

        numDocPaciente=PacienteActual.numDocumento
        
        messages.success(request, "No se pudo cargar el Biologico.")
        return redirect('/biologicos/'+numDocPaciente)


    PacienteActual=Paciente.objects.get(id=id)

    vacunaregistrar="NEUMOCOCO_CONJUGADO"

    match bio:
        case "1000":
            print("Unica")

        case "1001":
            print("1ra dosis")

        case "1002":
            print("2da dosis")

        case "1003":

            nombretabbio=NEUMOCON

            data={
                'biologico':'Neumococo Conjugado',
                'dosis':'3ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "1004":
            print("4ta dosis")

        case "1005":
            print("4ta dosis")

        case "1006":
            print("4ta dosis")

        case "1007":
            print("4ta dosis")

        case "1008":
            print("4ta dosis")

        case "2000":
            print("4ta dosis")

        case "2001":
            print("4ta dosis")

        case "2002":
            print("4ta dosis")

        case "2003":
            print("4ta dosis")

        case "2004":
            print("4ta dosis")

        case "2005":
            print("4ta dosis")

        case "2006":
            print("4ta dosis")

        case "2007":
            print("4ta dosis")

        case "2008":
            print("4ta dosis")

    print(id)
    print(NEUMOCON.objects.values_list('pk',flat=True))
    # si el paciente se encuentra en bd de vacuna...
    # if id in NEUMOCON.objects.values_list('pk', flat=True):
    if nombretabbio.objects.filter(pk=id).exists():

        tabbio=nombretabbio.objects.get(pk=id)

        print(data)

        datosaplibio={
        'laboratorio':tabbio.LABORATORIO,
        'lote':tabbio.LOTE,
        'fechavenvacu':tabbio.FECHAVENVACU,
        'tactivacu':tabbio.TACTIVAVACU,
        'fechaapli':tabbio.FECHAAPLI,
        'fechaprox':tabbio.FECHAPROX,
        'empresa':tabbio.EMPRESA,
        'condicionusuaria':tabbio.CONDICIONUSUARIA,
        'numfactura':tabbio.NUMFACTURA,
        }

        print('Ya existe esta aplicacion')

        data.update(datosaplibio)
        print(data)

        return render(request, 'vacunas/info_vacunas_aplicadas.html',data)

        

    else:
        print('no existe')
    
        return render(request, 'vacunas/info_vacunas.html',data)
    
    
