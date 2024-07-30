from paciente.models import Paciente
from django.shortcuts import render, redirect, Http404, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import VacunasPacientes
from django.contrib import messages
from vacunas.models import VacunasPacientes

from vacunas.models import *
from vacunas.forms import *
from json import dumps


# Create your views here.

def vacunas(request, cedula):

    paciente = get_list_or_404(Paciente, numDocumento=cedula)
    esquemavacpaciente=get_object_or_404(VacunasPacientes, pk=paciente[0].pk)


    edad = Paciente.calcularEdad(paciente[0])
    data = {
        'paciente': paciente[0],
        'edad': edad,   
        'DPT_ACELULAR_U':esquemavacpaciente.DPT_ACELULAR_U,
        'DPT_ACELULAR_1':esquemavacpaciente.DPT_ACELULAR_1,
        'DPT_ACELULAR_2':esquemavacpaciente.DPT_ACELULAR_2,
        'DPT_ACELULAR_3':esquemavacpaciente.DPT_ACELULAR_3,
        'DPT_ACELULAR_4':esquemavacpaciente.DPT_ACELULAR_4,
        'DPT_ACELULAR_5':esquemavacpaciente.DPT_ACELULAR_5,
        'DPT_ACELULAR_R1':esquemavacpaciente.DPT_ACELULAR_R1,
        'DPT_ACELULAR_R2':esquemavacpaciente.DPT_ACELULAR_R2,
        'DPT_ACELULAR_R3':esquemavacpaciente.DPT_ACELULAR_R3,
        'NEUMOCOCO_CONJUGADO_U':esquemavacpaciente.NEUMOCOCO_CONJUGADO_U,
        'NEUMOCOCO_CONJUGADO_1':esquemavacpaciente.NEUMOCOCO_CONJUGADO_1,
        'NEUMOCOCO_CONJUGADO_2':esquemavacpaciente.NEUMOCOCO_CONJUGADO_2,
        'NEUMOCOCO_CONJUGADO_3':esquemavacpaciente.NEUMOCOCO_CONJUGADO_3,
        'NEUMOCOCO_CONJUGADO_4':esquemavacpaciente.NEUMOCOCO_CONJUGADO_4,
        'NEUMOCOCO_CONJUGADO_5':esquemavacpaciente.NEUMOCOCO_CONJUGADO_5,
        'NEUMOCOCO_CONJUGADO_R1':esquemavacpaciente.NEUMOCOCO_CONJUGADO_R1,
        'NEUMOCOCO_CONJUGADO_R2':esquemavacpaciente.NEUMOCOCO_CONJUGADO_R2,
        'NEUMOCOCO_CONJUGADO_R3':esquemavacpaciente.NEUMOCOCO_CONJUGADO_R3,
        'MENINGOCOCO_U':esquemavacpaciente.MENINGOCOCO_U,
        'MENINGOCOCO_1':esquemavacpaciente.MENINGOCOCO_1,
        'MENINGOCOCO_2':esquemavacpaciente.MENINGOCOCO_2,
        'MENINGOCOCO_3':esquemavacpaciente.MENINGOCOCO_3,
        'MENINGOCOCO_4':esquemavacpaciente.MENINGOCOCO_4,
        'MENINGOCOCO_5':esquemavacpaciente.MENINGOCOCO_5,
        'MENINGOCOCO_R1':esquemavacpaciente.MENINGOCOCO_R1,
        'MENINGOCOCO_R2':esquemavacpaciente.MENINGOCOCO_R2,
        'MENINGOCOCO_R3':esquemavacpaciente.MENINGOCOCO_R3,
        'TRIPLE_VIRAL_U':esquemavacpaciente.TRIPLE_VIRAL_U,
        'TRIPLE_VIRAL_1':esquemavacpaciente.TRIPLE_VIRAL_1,
        'TRIPLE_VIRAL_2':esquemavacpaciente.TRIPLE_VIRAL_2,
        'TRIPLE_VIRAL_3':esquemavacpaciente.TRIPLE_VIRAL_3,
        'TRIPLE_VIRAL_4':esquemavacpaciente.TRIPLE_VIRAL_4,
        'TRIPLE_VIRAL_5':esquemavacpaciente.TRIPLE_VIRAL_5,
        'TRIPLE_VIRAL_R1':esquemavacpaciente.TRIPLE_VIRAL_R1,
        'TRIPLE_VIRAL_R2':esquemavacpaciente.TRIPLE_VIRAL_R2,
        'TRIPLE_VIRAL_R3':esquemavacpaciente.TRIPLE_VIRAL_R3,
        'VARICELA_U':esquemavacpaciente.VARICELA_U,
        'VARICELA_1':esquemavacpaciente.VARICELA_1,
        'VARICELA_2':esquemavacpaciente.VARICELA_2,
        'VARICELA_3':esquemavacpaciente.VARICELA_3,
        'VARICELA_4':esquemavacpaciente.VARICELA_4,
        'VARICELA_5':esquemavacpaciente.VARICELA_5,
        'VARICELA_R1':esquemavacpaciente.VARICELA_R1,
        'VARICELA_R2':esquemavacpaciente.VARICELA_R2,
        'VARICELA_R3':esquemavacpaciente.VARICELA_R3,
        'HEPATITIS_A_U':esquemavacpaciente.HEPATITIS_A_U,
        'HEPATITIS_A_1':esquemavacpaciente.HEPATITIS_A_1,
        'HEPATITIS_A_2':esquemavacpaciente.HEPATITIS_A_2,
        'HEPATITIS_A_3':esquemavacpaciente.HEPATITIS_A_3,
        'HEPATITIS_A_4':esquemavacpaciente.HEPATITIS_A_4,
        'HEPATITIS_A_5':esquemavacpaciente.HEPATITIS_A_5,
        'HEPATITIS_A_R1':esquemavacpaciente.HEPATITIS_A_R1,
        'HEPATITIS_A_R2':esquemavacpaciente.HEPATITIS_A_R2,
        'HEPATITIS_A_R3':esquemavacpaciente.HEPATITIS_A_R3,
        'FIEBRE_AMARILLA_U':esquemavacpaciente.FIEBRE_AMARILLA_U,
        'FIEBRE_AMARILLA_1':esquemavacpaciente.FIEBRE_AMARILLA_1,
        'FIEBRE_AMARILLA_2':esquemavacpaciente.FIEBRE_AMARILLA_2,
        'FIEBRE_AMARILLA_3':esquemavacpaciente.FIEBRE_AMARILLA_3,
        'FIEBRE_AMARILLA_4':esquemavacpaciente.FIEBRE_AMARILLA_4,
        'FIEBRE_AMARILLA_5':esquemavacpaciente.FIEBRE_AMARILLA_5,
        'FIEBRE_AMARILLA_R1':esquemavacpaciente.FIEBRE_AMARILLA_R1,
        'FIEBRE_AMARILLA_R2':esquemavacpaciente.FIEBRE_AMARILLA_R2,
        'FIEBRE_AMARILLA_R3':esquemavacpaciente.FIEBRE_AMARILLA_R3,
        'INFLUENZA_U':esquemavacpaciente.INFLUENZA_U,
        'INFLUENZA_1':esquemavacpaciente.INFLUENZA_1,
        'INFLUENZA_2':esquemavacpaciente.INFLUENZA_2,
        'INFLUENZA_3':esquemavacpaciente.INFLUENZA_3,
        'INFLUENZA_4':esquemavacpaciente.INFLUENZA_4,
        'INFLUENZA_5':esquemavacpaciente.INFLUENZA_5,
        'INFLUENZA_R1':esquemavacpaciente.INFLUENZA_R1,
        'INFLUENZA_R2':esquemavacpaciente.INFLUENZA_R2,
        'INFLUENZA_R3':esquemavacpaciente.INFLUENZA_R3,
        'COVID_U':esquemavacpaciente.COVID_U,
        'COVID_1':esquemavacpaciente.COVID_1,
        'COVID_2':esquemavacpaciente.COVID_2,
        'COVID_3':esquemavacpaciente.COVID_3,
        'COVID_4':esquemavacpaciente.COVID_4,
        'COVID_5':esquemavacpaciente.COVID_5,
        'COVID_R1':esquemavacpaciente.COVID_R1,
        'COVID_R2':esquemavacpaciente.COVID_R2,
        'COVID_R3':esquemavacpaciente.COVID_R3,
        'HERPES_ZOSTER_U':esquemavacpaciente.HERPES_ZOSTER_U,
        'HERPES_ZOSTER_1':esquemavacpaciente.HERPES_ZOSTER_1,
        'HERPES_ZOSTER_2':esquemavacpaciente.HERPES_ZOSTER_2,
        'HERPES_ZOSTER_3':esquemavacpaciente.HERPES_ZOSTER_3,
        'HERPES_ZOSTER_4':esquemavacpaciente.HERPES_ZOSTER_4,
        'HERPES_ZOSTER_5':esquemavacpaciente.HERPES_ZOSTER_5,
        'HERPES_ZOSTER_R1':esquemavacpaciente.HERPES_ZOSTER_R1,
        'HERPES_ZOSTER_R2':esquemavacpaciente.HERPES_ZOSTER_R2,
        'HERPES_ZOSTER_R3':esquemavacpaciente.HERPES_ZOSTER_R3,
        'HEPATITIS_B_U':esquemavacpaciente.HEPATITIS_B_U,
        'HEPATITIS_B_1':esquemavacpaciente.HEPATITIS_B_1,
        'HEPATITIS_B_2':esquemavacpaciente.HEPATITIS_B_2,
        'HEPATITIS_B_3':esquemavacpaciente.HEPATITIS_B_3,
        'HEPATITIS_B_4':esquemavacpaciente.HEPATITIS_B_4,
        'HEPATITIS_B_5':esquemavacpaciente.HEPATITIS_B_5,
        'HEPATITIS_B_R1':esquemavacpaciente.HEPATITIS_B_R1,
        'HEPATITIS_B_R2':esquemavacpaciente.HEPATITIS_B_R2,
        'HEPATITIS_B_R3':esquemavacpaciente.HEPATITIS_B_R3,
        'ANTIRRABICA_U':esquemavacpaciente.ANTIRRABICA_U,
        'ANTIRRABICA_1':esquemavacpaciente.ANTIRRABICA_1,
        'ANTIRRABICA_2':esquemavacpaciente.ANTIRRABICA_2,
        'ANTIRRABICA_3':esquemavacpaciente.ANTIRRABICA_3,
        'ANTIRRABICA_4':esquemavacpaciente.ANTIRRABICA_4,
        'ANTIRRABICA_5':esquemavacpaciente.ANTIRRABICA_5,
        'ANTIRRABICA_R1':esquemavacpaciente.ANTIRRABICA_R1,
        'ANTIRRABICA_R2':esquemavacpaciente.ANTIRRABICA_R2,
        'ANTIRRABICA_R3':esquemavacpaciente.ANTIRRABICA_R3,
        'VPH_U':esquemavacpaciente.VPH_U,
        'VPH_1':esquemavacpaciente.VPH_1,
        'VPH_2':esquemavacpaciente.VPH_2,
        'VPH_3':esquemavacpaciente.VPH_3,
        'VPH_4':esquemavacpaciente.VPH_4,
        'VPH_5':esquemavacpaciente.VPH_5,
        'VPH_R1':esquemavacpaciente.VPH_R1,
        'VPH_R2':esquemavacpaciente.VPH_R2,
        'VPH_R3':esquemavacpaciente.VPH_R3,
        'HA_HB_U':esquemavacpaciente.HA_HB_U,
        'HA_HB_1':esquemavacpaciente.HA_HB_1,
        'HA_HB_2':esquemavacpaciente.HA_HB_2,
        'HA_HB_3':esquemavacpaciente.HA_HB_3,
        'HA_HB_4':esquemavacpaciente.HA_HB_4,
        'HA_HB_5':esquemavacpaciente.HA_HB_5,
        'HA_HB_R1':esquemavacpaciente.HA_HB_R1,
        'HA_HB_R2':esquemavacpaciente.HA_HB_R2,
        'HA_HB_R3':esquemavacpaciente.HA_HB_R3,
        'TETANO_ANTITETANICA_U':esquemavacpaciente.TETANO_ANTITETANICA_U,
        'TETANO_ANTITETANICA_1':esquemavacpaciente.TETANO_ANTITETANICA_1,
        'TETANO_ANTITETANICA_2':esquemavacpaciente.TETANO_ANTITETANICA_2,
        'TETANO_ANTITETANICA_3':esquemavacpaciente.TETANO_ANTITETANICA_3,
        'TETANO_ANTITETANICA_4':esquemavacpaciente.TETANO_ANTITETANICA_4,
        'TETANO_ANTITETANICA_5':esquemavacpaciente.TETANO_ANTITETANICA_5,
        'TETANO_ANTITETANICA_R1':esquemavacpaciente.TETANO_ANTITETANICA_R1,
        'TETANO_ANTITETANICA_R2':esquemavacpaciente.TETANO_ANTITETANICA_R2,
        'TETANO_ANTITETANICA_R3':esquemavacpaciente.TETANO_ANTITETANICA_R3,
        'TETANO_DIFTERICO_U':esquemavacpaciente.TETANO_DIFTERICO_U,
        'TETANO_DIFTERICO_1':esquemavacpaciente.TETANO_DIFTERICO_1,
        'TETANO_DIFTERICO_2':esquemavacpaciente.TETANO_DIFTERICO_2,
        'TETANO_DIFTERICO_3':esquemavacpaciente.TETANO_DIFTERICO_3,
        'TETANO_DIFTERICO_4':esquemavacpaciente.TETANO_DIFTERICO_4,
        'TETANO_DIFTERICO_5':esquemavacpaciente.TETANO_DIFTERICO_5,
        'TETANO_DIFTERICO_R1':esquemavacpaciente.TETANO_DIFTERICO_R1,
        'TETANO_DIFTERICO_R2':esquemavacpaciente.TETANO_DIFTERICO_R2,
        'TETANO_DIFTERICO_R3':esquemavacpaciente.TETANO_DIFTERICO_R3,
        'FIEBRE_TIFOIDEA_U':esquemavacpaciente.FIEBRE_TIFOIDEA_U,
        'FIEBRE_TIFOIDEA_1':esquemavacpaciente.FIEBRE_TIFOIDEA_1,
        'FIEBRE_TIFOIDEA_2':esquemavacpaciente.FIEBRE_TIFOIDEA_2,
        'FIEBRE_TIFOIDEA_3':esquemavacpaciente.FIEBRE_TIFOIDEA_3,
        'FIEBRE_TIFOIDEA_4':esquemavacpaciente.FIEBRE_TIFOIDEA_4,
        'FIEBRE_TIFOIDEA_5':esquemavacpaciente.FIEBRE_TIFOIDEA_5,
        'FIEBRE_TIFOIDEA_R1':esquemavacpaciente.FIEBRE_TIFOIDEA_R1,
        'FIEBRE_TIFOIDEA_R2':esquemavacpaciente.FIEBRE_TIFOIDEA_R2,
        'FIEBRE_TIFOIDEA_R3':esquemavacpaciente.FIEBRE_TIFOIDEA_R3,



    }
    print(data)
    
    return render(request, 'vacunas/lista_vacunas.html', data)


    
def infova(request, id, bio):

    
    if request.method == 'POST':
        
        match bio:
            case "1000":
                nombreform=NEUMOCOCO
                vacunaregistrar="NEUMOCOCO_CONJUGADO_U"

            case "1001":
                nombreform=NEUMOCOCO1
                vacunaregistrar="NEUMOCOCO_CONJUGADO_1"

            case "1002":
                nombreform=NEUMOCOCO2
                vacunaregistrar="NEUMOCOCO_CONJUGADO_2"

            case "1003":
                nombreform=NEUMOCOCO3
                vacunaregistrar="NEUMOCOCO_CONJUGADO_3"

            case "1004":
                nombreform=NEUMOCOCO4
                vacunaregistrar="NEUMOCOCO_CONJUGADO_4"

            case "1005":
                nombreform=NEUMOCOCO5
                vacunaregistrar="NEUMOCOCO_CONJUGADO_5"

            case "1006":
                nombreform=NEUMOCOCOR1
                vacunaregistrar="NEUMOCOCO_CONJUGADO_R1"

            case "1007":
                nombreform=NEUMOCOCOR2
                vacunaregistrar="NEUMOCOCO_CONJUGADO_R2"

            case "1008":
                nombreform=NEUMOCOCOR3
                vacunaregistrar="NEUMOCOCO_CONJUGADO_R3"

        # se crea instancia de formulario y se guarda la data del post
        formulario = nombreform(data=request.POST)

        print(formulario.errors)
        if formulario.is_valid():
            #Completo el paciente
            formulario.instance.PACIENTE = get_object_or_404(Paciente, id=id)
            nombreusuario=str(request.user)
            formulario.instance.NOMBREVACUNADOR=nombreusuario

            formulario.save()
  
            # Marca la vacuna como aplicada en esquema
            
            esquemapaciente=VacunasPacientes.objects.get(PACIENTE_id=id)

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

    

    match bio:
        case "1000":
            nombretabbio=NEUMOCON

            data={
                'biologico':'Neumococo Conjugado',
                'dosis':'Unica',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "1001":
            nombretabbio=NEUMOCON1

            data={
                'biologico':'Neumococo Conjugado',
                'dosis':'1ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "1002":
            nombretabbio=NEUMOCON2

            data={
                'biologico':'Neumococo Conjugado',
                'dosis':'2da Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "1003":

            nombretabbio=NEUMOCON3

            data={
                'biologico':'Neumococo Conjugado',
                'dosis':'3ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "1004":
            nombretabbio=NEUMOCON4

            data={
                'biologico':'Neumococo Conjugado',
                'dosis':'4ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "1005":
            nombretabbio=NEUMOCON5

            data={
                'biologico':'Neumococo Conjugado',
                'dosis':'5ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "1006":
            nombretabbio=NEUMOCONR1

            data={
                'biologico':'Neumococo Conjugado',
                'dosis':'1er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "1007":
            nombretabbio=NEUMOCONR2

            data={
                'biologico':'Neumococo Conjugado',
                'dosis':'2do Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "1008":
            nombretabbio=NEUMOCONR3

            data={
                'biologico':'Neumococo Conjugado',
                'dosis':'3er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }


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

    print(nombretabbio.objects.filter(pk=id))

    # si el paciente se encuentra en bd de vacuna...
    # if id in NEUMOCON.objects.values_list('pk', flat=True):
    if nombretabbio.objects.filter(pk=id).exists():

        tabbio=nombretabbio.objects.get(pk=id)

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
    
    
