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

            case "17000":
                nombreform=DPT_ACELULAR_U
                vacunaregistrar="DPT_ACELULAR_U"

            case "17001":
                nombreform=DPT_ACELULAR_1
                vacunaregistrar="DPT_ACELULAR_1"

            case "17002":
                nombreform=DPT_ACELULAR_2
                vacunaregistrar="DPT_ACELULAR_2"

            case "17003":
                nombreform=DPT_ACELULAR_3
                vacunaregistrar="DPT_ACELULAR_3"

            case "17004":
                nombreform=DPT_ACELULAR_4
                vacunaregistrar="DPT_ACELULAR_4"

            case "17005":
                nombreform=DPT_ACELULAR_5
                vacunaregistrar="DPT_ACELULAR_5"

            case "17006":
                nombreform=DPT_ACELULAR_R1
                vacunaregistrar="DPT_ACELULAR_R1"

            case "17007":
                nombreform=DPT_ACELULAR_R2
                vacunaregistrar="DPT_ACELULAR_R2"

            case "17008":
                nombreform=DPT_ACELULAR_R3
                vacunaregistrar="DPT_ACELULAR_R3"


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




            case "2000":
                nombreform=MENINGOCOCO_U
                vacunaregistrar="MENINGOCOCO_U"

            case "2001":
                nombreform=MENINGOCOCO_1
                vacunaregistrar="MENINGOCOCO_1"

            case "2002":
                nombreform=MENINGOCOCO_2
                vacunaregistrar="MENINGOCOCO_2"

            case "2003":
                nombreform=MENINGOCOCO_3
                vacunaregistrar="MENINGOCOCO_3"

            case "2004":
                nombreform=MENINGOCOCO_4
                vacunaregistrar="MENINGOCOCO_4"

            case "2005":
                nombreform=MENINGOCOCO_5
                vacunaregistrar="MENINGOCOCO_5"

            case "2006":
                nombreform=MENINGOCOCO_R1
                vacunaregistrar="MENINGOCOCO_R1"

            case "2007":
                nombreform=MENINGOCOCO_R2
                vacunaregistrar="MENINGOCOCO_R2"

            case "2008":
                nombreform=MENINGOCOCO_R3
                vacunaregistrar="MENINGOCOCO_R3"

            case "3000":
                nombreform=TRIPLE_VIRAL_U
                vacunaregistrar="TRIPLE_VIRAL_U"

            case "3001":
                nombreform=TRIPLE_VIRAL_1
                vacunaregistrar="TRIPLE_VIRAL_1"

            case "3002":
                nombreform=TRIPLE_VIRAL_2
                vacunaregistrar="TRIPLE_VIRAL_2"

            case "3003":
                nombreform=TRIPLE_VIRAL_3
                vacunaregistrar="TRIPLE_VIRAL_3"

            case "3004":
                nombreform=TRIPLE_VIRAL_4
                vacunaregistrar="TRIPLE_VIRAL_4"

            case "3005":
                nombreform=TRIPLE_VIRAL_5
                vacunaregistrar="TRIPLE_VIRAL_5"

            case "3006":
                nombreform=TRIPLE_VIRAL_R1
                vacunaregistrar="TRIPLE_VIRAL_R1"

            case "3007":
                nombreform=TRIPLE_VIRAL_R2
                vacunaregistrar="TRIPLE_VIRAL_R2"

            case "3008":
                nombreform=TRIPLE_VIRAL_R3
                vacunaregistrar="TRIPLE_VIRAL_R3"



            case "4000":
                nombreform=VARICELA_U
                vacunaregistrar="VARICELA_U"

            case "4001":
                nombreform=VARICELA_1
                vacunaregistrar="VARICELA_1"

            case "4002":
                nombreform=VARICELA_2
                vacunaregistrar="VARICELA_2"

            case "4003":
                nombreform=VARICELA_3
                vacunaregistrar="VARICELA_3"

            case "4004":
                nombreform=VARICELA_4
                vacunaregistrar="VARICELA_4"

            case "4005":
                nombreform=VARICELA_5
                vacunaregistrar="VARICELA_5"

            case "4006":
                nombreform=VARICELA_R1
                vacunaregistrar="VARICELA_R1"

            case "4007":
                nombreform=VARICELA_R2
                vacunaregistrar="VARICELA_R2"

            case "4008":
                nombreform=VARICELA_R3
                vacunaregistrar="VARICELA_R3"

            case "5000":
                nombreform=HEPATITIS_A_U
                vacunaregistrar="HEPATITIS_A_U"

            case "5001":
                nombreform=HEPATITIS_A_1
                vacunaregistrar="HEPATITIS_A_1"

            case "5002":
                nombreform=HEPATITIS_A_2
                vacunaregistrar="HEPATITIS_A_2"

            case "5003":
                nombreform=HEPATITIS_A_3
                vacunaregistrar="HEPATITIS_A_3"

            case "5004":
                nombreform=HEPATITIS_A_4
                vacunaregistrar="HEPATITIS_A_4"

            case "5005":
                nombreform=HEPATITIS_A_5
                vacunaregistrar="HEPATITIS_A_5"

            case "5006":
                nombreform=HEPATITIS_A_R1
                vacunaregistrar="HEPATITIS_A_R1"

            case "5007":
                nombreform=HEPATITIS_A_R2
                vacunaregistrar="HEPATITIS_A_R2"

            case "5008":
                nombreform=HEPATITIS_A_R3
                vacunaregistrar="HEPATITIS_A_R3"

            case "6000":
                nombreform=FIEBRE_AMARILLA_U
                vacunaregistrar="FIEBRE_AMARILLA_U"

            case "6001":
                nombreform=FIEBRE_AMARILLA_1
                vacunaregistrar="FIEBRE_AMARILLA_1"

            case "6002":
                nombreform=FIEBRE_AMARILLA_2
                vacunaregistrar="FIEBRE_AMARILLA_2"

            case "6003":
                nombreform=FIEBRE_AMARILLA_3
                vacunaregistrar="FIEBRE_AMARILLA_3"

            case "6004":
                nombreform=FIEBRE_AMARILLA_4
                vacunaregistrar="FIEBRE_AMARILLA_4"

            case "6005":
                nombreform=FIEBRE_AMARILLA_5
                vacunaregistrar="FIEBRE_AMARILLA_5"

            case "6006":
                nombreform=FIEBRE_AMARILLA_R1
                vacunaregistrar="FIEBRE_AMARILLA_R1"

            case "6007":
                nombreform=FIEBRE_AMARILLA_R2
                vacunaregistrar="FIEBRE_AMARILLA_R2"

            case "6008":
                nombreform=FIEBRE_AMARILLA_R3
                vacunaregistrar="FIEBRE_AMARILLA_R3"

            case "7000":
                nombreform=INFLUENZA_U
                vacunaregistrar="INFLUENZA_U"

            case "7001":
                nombreform=INFLUENZA_1
                vacunaregistrar="INFLUENZA_1"

            case "7002":
                nombreform=INFLUENZA_2
                vacunaregistrar="INFLUENZA_2"

            case "7003":
                nombreform=INFLUENZA_3
                vacunaregistrar="INFLUENZA_3"

            case "7004":
                nombreform=INFLUENZA_4
                vacunaregistrar="INFLUENZA_4"

            case "7005":
                nombreform=INFLUENZA_5
                vacunaregistrar="INFLUENZA_5"

            case "7006":
                nombreform=INFLUENZA_R1
                vacunaregistrar="INFLUENZA_R1"

            case "7007":
                nombreform=INFLUENZA_R2
                vacunaregistrar="INFLUENZA_R2"

            case "7008":
                nombreform=INFLUENZA_R3
                vacunaregistrar="INFLUENZA_R3"

            case "8000":
                nombreform=COVID_U
                vacunaregistrar="COVID_U"

            case "8001":
                nombreform=COVID_1
                vacunaregistrar="COVID_1"

            case "8002":
                nombreform=COVID_2
                vacunaregistrar="COVID_2"

            case "8003":
                nombreform=COVID_3
                vacunaregistrar="COVID_3"

            case "8004":
                nombreform=COVID_4
                vacunaregistrar="COVID_4"

            case "8005":
                nombreform=COVID_5
                vacunaregistrar="COVID_5"

            case "8006":
                nombreform=COVID_R1
                vacunaregistrar="COVID_R1"

            case "8007":
                nombreform=COVID_R2
                vacunaregistrar="COVID_R2"

            case "8008":
                nombreform=COVID_R3
                vacunaregistrar="COVID_R3"

            case "9000":
                nombreform=HERPES_ZOSTER_U
                vacunaregistrar="HERPES_ZOSTER_U"

            case "9001":
                nombreform=HERPES_ZOSTER_1
                vacunaregistrar="HERPES_ZOSTER_1"

            case "9002":
                nombreform=HERPES_ZOSTER_2
                vacunaregistrar="HERPES_ZOSTER_2"

            case "9003":
                nombreform=HERPES_ZOSTER_3
                vacunaregistrar="HERPES_ZOSTER_3"

            case "9004":
                nombreform=HERPES_ZOSTER_4
                vacunaregistrar="HERPES_ZOSTER_4"

            case "9005":
                nombreform=HERPES_ZOSTER_5
                vacunaregistrar="HERPES_ZOSTER_5"

            case "9006":
                nombreform=HERPES_ZOSTER_R1
                vacunaregistrar="HERPES_ZOSTER_R1"

            case "9007":
                nombreform=HERPES_ZOSTER_R2
                vacunaregistrar="HERPES_ZOSTER_R2"

            case "9008":
                nombreform=HERPES_ZOSTER_R3
                vacunaregistrar="HERPES_ZOSTER_R3"

            case "10000":
                nombreform=HEPATITIS_B_U
                vacunaregistrar="HEPATITIS_B_U"

            case "10001":
                nombreform=HEPATITIS_B_1
                vacunaregistrar="HEPATITIS_B_1"

            case "10002":
                nombreform=HEPATITIS_B_2
                vacunaregistrar="HEPATITIS_B_2"

            case "10003":
                nombreform=HEPATITIS_B_3
                vacunaregistrar="HEPATITIS_B_3"

            case "10004":
                nombreform=HEPATITIS_B_4
                vacunaregistrar="HEPATITIS_B_4"

            case "10005":
                nombreform=HEPATITIS_B_5
                vacunaregistrar="HEPATITIS_B_5"

            case "10006":
                nombreform=HEPATITIS_B_R1
                vacunaregistrar="HEPATITIS_B_R1"

            case "10007":
                nombreform=HEPATITIS_B_R2
                vacunaregistrar="HEPATITIS_B_R2"

            case "10008":
                nombreform=HEPATITIS_B_R3
                vacunaregistrar="HEPATITIS_B_R3"

            case "11000":
                nombreform=ANTIRRABICA_U
                vacunaregistrar="ANTIRRABICA_U"

            case "11001":
                nombreform=ANTIRRABICA_1
                vacunaregistrar="ANTIRRABICA_1"

            case "11002":
                nombreform=ANTIRRABICA_2
                vacunaregistrar="ANTIRRABICA_2"

            case "11003":
                nombreform=ANTIRRABICA_3
                vacunaregistrar="ANTIRRABICA_3"

            case "11004":
                nombreform=ANTIRRABICA_4
                vacunaregistrar="ANTIRRABICA_4"

            case "11005":
                nombreform=ANTIRRABICA_5
                vacunaregistrar="ANTIRRABICA_5"

            case "11006":
                nombreform=ANTIRRABICA_R1
                vacunaregistrar="ANTIRRABICA_R1"

            case "11007":
                nombreform=ANTIRRABICA_R2
                vacunaregistrar="ANTIRRABICA_R2"

            case "11008":
                nombreform=ANTIRRABICA_R3
                vacunaregistrar="ANTIRRABICA_R3"

            case "12000":
                nombreform=VPH_U
                vacunaregistrar="VPH_U"

            case "12001":
                nombreform=VPH_1
                vacunaregistrar="VPH_1"

            case "12002":
                nombreform=VPH_2
                vacunaregistrar="VPH_2"

            case "12003":
                nombreform=VPH_3
                vacunaregistrar="VPH_3"

            case "12004":
                nombreform=VPH_4
                vacunaregistrar="VPH_4"

            case "12005":
                nombreform=VPH_5
                vacunaregistrar="VPH_5"

            case "12006":
                nombreform=VPH_R1
                vacunaregistrar="VPH_R1"

            case "12007":
                nombreform=VPH_R2
                vacunaregistrar="VPH_R2"

            case "12008":
                nombreform=VPH_R3
                vacunaregistrar="VPH_R3"

            case "13000":
                nombreform=HA_HB_U
                vacunaregistrar="HA_HB_U"

            case "13001":
                nombreform=HA_HB_1
                vacunaregistrar="HA_HB_1"

            case "13002":
                nombreform=HA_HB_2
                vacunaregistrar="HA_HB_2"

            case "13003":
                nombreform=HA_HB_3
                vacunaregistrar="HA_HB_3"

            case "13004":
                nombreform=HA_HB_4
                vacunaregistrar="HA_HB_4"

            case "13005":
                nombreform=HA_HB_5
                vacunaregistrar="HA_HB_5"

            case "13006":
                nombreform=HA_HB_R1
                vacunaregistrar="HA_HB_R1"

            case "13007":
                nombreform=HA_HB_R2
                vacunaregistrar="HA_HB_R2"

            case "13008":
                nombreform=HA_HB_R3
                vacunaregistrar="HA_HB_R3"

            case "14000":
                nombreform=TETANO_ANTITETANICA_U
                vacunaregistrar="TETANO_ANTITETANICA_U"

            case "14001":
                nombreform=TETANO_ANTITETANICA_1
                vacunaregistrar="TETANO_ANTITETANICA_1"

            case "14002":
                nombreform=TETANO_ANTITETANICA_2
                vacunaregistrar="TETANO_ANTITETANICA_2"

            case "14003":
                nombreform=TETANO_ANTITETANICA_3
                vacunaregistrar="TETANO_ANTITETANICA_3"

            case "14004":
                nombreform=TETANO_ANTITETANICA_4
                vacunaregistrar="TETANO_ANTITETANICA_4"

            case "14005":
                nombreform=TETANO_ANTITETANICA_5
                vacunaregistrar="TETANO_ANTITETANICA_5"

            case "14006":
                nombreform=TETANO_ANTITETANICA_R1
                vacunaregistrar="TETANO_ANTITETANICA_R1"

            case "14007":
                nombreform=TETANO_ANTITETANICA_R2
                vacunaregistrar="TETANO_ANTITETANICA_R2"

            case "14008":
                nombreform=TETANO_ANTITETANICA_R3
                vacunaregistrar="TETANO_ANTITETANICA_R3"

            case "15000":
                nombreform=TETANO_DIFTERICO_U
                vacunaregistrar="TETANO_DIFTERICO_U"

            case "15001":
                nombreform=TETANO_DIFTERICO_1
                vacunaregistrar="TETANO_DIFTERICO_1"

            case "15002":
                nombreform=TETANO_DIFTERICO_2
                vacunaregistrar="TETANO_DIFTERICO_2"

            case "15003":
                nombreform=TETANO_DIFTERICO_3
                vacunaregistrar="TETANO_DIFTERICO_3"

            case "15004":
                nombreform=TETANO_DIFTERICO_4
                vacunaregistrar="TETANO_DIFTERICO_4"

            case "15005":
                nombreform=TETANO_DIFTERICO_5
                vacunaregistrar="TETANO_DIFTERICO_5"

            case "15006":
                nombreform=TETANO_DIFTERICO_R1
                vacunaregistrar="TETANO_DIFTERICO_R1"

            case "15007":
                nombreform=TETANO_DIFTERICO_R2
                vacunaregistrar="TETANO_DIFTERICO_R2"

            case "15008":
                nombreform=TETANO_DIFTERICO_R3
                vacunaregistrar="TETANO_DIFTERICO_R3"

            case "16000":
                nombreform=FIEBRE_TIFOIDEA_U
                vacunaregistrar="FIEBRE_TIFOIDEA_U"

            case "16001":
                nombreform=FIEBRE_TIFOIDEA_1
                vacunaregistrar="FIEBRE_TIFOIDEA_1"

            case "16002":
                nombreform=FIEBRE_TIFOIDEA_2
                vacunaregistrar="FIEBRE_TIFOIDEA_2"

            case "16003":
                nombreform=FIEBRE_TIFOIDEA_3
                vacunaregistrar="FIEBRE_TIFOIDEA_3"

            case "16004":
                nombreform=FIEBRE_TIFOIDEA_4
                vacunaregistrar="FIEBRE_TIFOIDEA_4"

            case "16005":
                nombreform=FIEBRE_TIFOIDEA_5
                vacunaregistrar="FIEBRE_TIFOIDEA_5"

            case "16006":
                nombreform=FIEBRE_TIFOIDEA_R1
                vacunaregistrar="FIEBRE_TIFOIDEA_R1"

            case "16007":
                nombreform=FIEBRE_TIFOIDEA_R2
                vacunaregistrar="FIEBRE_TIFOIDEA_R2"

            case "16008":
                nombreform=FIEBRE_TIFOIDEA_R3
                vacunaregistrar="FIEBRE_TIFOIDEA_R3"


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

        case "17000":
            nombretabbio=T_DPT_ACELULAR_U

            data={
                'biologico':'DPT ACELULAR',
                'dosis':'Unica',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "17001":
            nombretabbio=T_DPT_ACELULAR_1

            data={
                'biologico':'DPT ACELULAR',
                'dosis':'1ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "17002":
            nombretabbio=T_DPT_ACELULAR_2

            data={
                'biologico':'DPT ACELULAR',
                'dosis':'2da Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "17003":
            nombretabbio=T_DPT_ACELULAR_3

            data={
                'biologico':'DPT ACELULAR',
                'dosis':'3ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "17004":
            nombretabbio=T_DPT_ACELULAR_4

            data={
                'biologico':'DPT ACELULAR',
                'dosis':'4ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "17005":
            nombretabbio=T_DPT_ACELULAR_5

            data={
                'biologico':'DPT ACELULAR',
                'dosis':'5ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "17006":
            nombretabbio=T_DPT_ACELULAR_R1

            data={
                'biologico':'DPT ACELULAR',
                'dosis':'1er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "17007":
            nombretabbio=T_DPT_ACELULAR_R2

            data={
                'biologico':'DPT ACELULAR',
                'dosis':'2do Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "17008":
            nombretabbio=T_DPT_ACELULAR_R3

            data={
                'biologico':'DPT ACELULAR',
                'dosis':'3er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

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
            nombretabbio=T_MENINGOCOCO_U

            data={
                'biologico':'MENINGOCOCO',
                'dosis':'Unica',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "2001":
            nombretabbio=T_MENINGOCOCO_1

            data={
                'biologico':'MENINGOCOCO',
                'dosis':'1ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "2002":
            nombretabbio=T_MENINGOCOCO_2

            data={
                'biologico':'MENINGOCOCO',
                'dosis':'2da Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "2003":
            nombretabbio=T_MENINGOCOCO_3

            data={
                'biologico':'MENINGOCOCO',
                'dosis':'3ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "2004":
            nombretabbio=T_MENINGOCOCO_4

            data={
                'biologico':'MENINGOCOCO',
                'dosis':'4ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "2005":
            nombretabbio=T_MENINGOCOCO_5

            data={
                'biologico':'MENINGOCOCO',
                'dosis':'5ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "2006":
            nombretabbio=T_MENINGOCOCO_R1

            data={
                'biologico':'MENINGOCOCO',
                'dosis':'1er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "2007":
            nombretabbio=T_MENINGOCOCO_R2

            data={
                'biologico':'MENINGOCOCO',
                'dosis':'2do Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "2008":
            nombretabbio=T_MENINGOCOCO_R3

            data={
                'biologico':'MENINGOCOCO',
                'dosis':'3er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "3000":
            nombretabbio=T_TRIPLE_VIRAL_U

            data={
                'biologico':'TRIPLE VIRAL',
                'dosis':'Unica',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "3001":
            nombretabbio=T_TRIPLE_VIRAL_1

            data={
                'biologico':'TRIPLE VIRAL',
                'dosis':'1ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "3002":
            nombretabbio=T_TRIPLE_VIRAL_2

            data={
                'biologico':'TRIPLE VIRAL',
                'dosis':'2da Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "3003":
            nombretabbio=T_TRIPLE_VIRAL_3

            data={
                'biologico':'TRIPLE VIRAL',
                'dosis':'3ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "3004":
            nombretabbio=T_TRIPLE_VIRAL_4

            data={
                'biologico':'TRIPLE VIRAL',
                'dosis':'4ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "3005":
            nombretabbio=T_TRIPLE_VIRAL_5

            data={
                'biologico':'TRIPLE VIRAL',
                'dosis':'5ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "3006":
            nombretabbio=T_TRIPLE_VIRAL_R1

            data={
                'biologico':'TRIPLE VIRAL',
                'dosis':'1er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "3007":
            nombretabbio=T_TRIPLE_VIRAL_R2

            data={
                'biologico':'TRIPLE VIRAL',
                'dosis':'2do Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "3008":
            nombretabbio=T_TRIPLE_VIRAL_R3

            data={
                'biologico':'TRIPLE VIRAL',
                'dosis':'3er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "4000":
            nombretabbio=T_VARICELA_U

            data={
                'biologico':'VARICELA',
                'dosis':'Unica',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "4001":
            nombretabbio=T_VARICELA_1

            data={
                'biologico':'VARICELA',
                'dosis':'1ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "4002":
            nombretabbio=T_VARICELA_2

            data={
                'biologico':'VARICELA',
                'dosis':'2da Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "4003":
            nombretabbio=T_VARICELA_3

            data={
                'biologico':'VARICELA',
                'dosis':'3ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "4004":
            nombretabbio=T_VARICELA_4

            data={
                'biologico':'VARICELA',
                'dosis':'4ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "4005":
            nombretabbio=T_VARICELA_5

            data={
                'biologico':'VARICELA',
                'dosis':'5ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "4006":
            nombretabbio=T_VARICELA_R1

            data={
                'biologico':'VARICELA',
                'dosis':'1er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "4007":
            nombretabbio=T_VARICELA_R2

            data={
                'biologico':'VARICELA',
                'dosis':'2do Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "4008":
            nombretabbio=T_VARICELA_R3

            data={
                'biologico':'VARICELA',
                'dosis':'3er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "5000":
            nombretabbio=T_HEPATITIS_A_U

            data={
                'biologico':'HEPATITIS A',
                'dosis':'Unica',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "5001":
            nombretabbio=T_HEPATITIS_A_1

            data={
                'biologico':'HEPATITIS A',
                'dosis':'1ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "5002":
            nombretabbio=T_HEPATITIS_A_2

            data={
                'biologico':'HEPATITIS A',
                'dosis':'2da Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "5003":
            nombretabbio=T_HEPATITIS_A_3

            data={
                'biologico':'HEPATITIS A',
                'dosis':'3ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "5004":
            nombretabbio=T_HEPATITIS_A_4

            data={
                'biologico':'HEPATITIS A',
                'dosis':'4ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "5005":
            nombretabbio=T_HEPATITIS_A_5

            data={
                'biologico':'HEPATITIS A',
                'dosis':'5ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "5006":
            nombretabbio=T_HEPATITIS_A_R1

            data={
                'biologico':'HEPATITIS A',
                'dosis':'1er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "5007":
            nombretabbio=T_HEPATITIS_A_R2

            data={
                'biologico':'HEPATITIS A',
                'dosis':'2do Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "5008":
            nombretabbio=T_HEPATITIS_A_R3

            data={
                'biologico':'HEPATITIS A',
                'dosis':'3er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "6000":
            nombretabbio=T_FIEBRE_AMARILLA_U

            data={
                'biologico':'FIEBRE AMARILLA',
                'dosis':'Unica',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "6001":
            nombretabbio=T_FIEBRE_AMARILLA_1

            data={
                'biologico':'FIEBRE AMARILLA',
                'dosis':'1ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "6002":
            nombretabbio=T_FIEBRE_AMARILLA_2

            data={
                'biologico':'FIEBRE AMARILLA',
                'dosis':'2da Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "6003":
            nombretabbio=T_FIEBRE_AMARILLA_3

            data={
                'biologico':'FIEBRE AMARILLA',
                'dosis':'3ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "6004":
            nombretabbio=T_FIEBRE_AMARILLA_4

            data={
                'biologico':'FIEBRE AMARILLA',
                'dosis':'4ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "6005":
            nombretabbio=T_FIEBRE_AMARILLA_5

            data={
                'biologico':'FIEBRE AMARILLA',
                'dosis':'5ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "6006":
            nombretabbio=T_FIEBRE_AMARILLA_R1

            data={
                'biologico':'FIEBRE AMARILLA',
                'dosis':'1er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "6007":
            nombretabbio=T_FIEBRE_AMARILLA_R2

            data={
                'biologico':'FIEBRE AMARILLA',
                'dosis':'2do Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "6008":
            nombretabbio=T_FIEBRE_AMARILLA_R3

            data={
                'biologico':'FIEBRE AMARILLA',
                'dosis':'3er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "7000":
            nombretabbio=T_INFLUENZA_U

            data={
                'biologico':'INFLUENZA',
                'dosis':'Unica',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "7001":
            nombretabbio=T_INFLUENZA_1

            data={
                'biologico':'INFLUENZA',
                'dosis':'1ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "7002":
            nombretabbio=T_INFLUENZA_2

            data={
                'biologico':'INFLUENZA',
                'dosis':'2da Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "7003":
            nombretabbio=T_INFLUENZA_3

            data={
                'biologico':'INFLUENZA',
                'dosis':'3ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "7004":
            nombretabbio=T_INFLUENZA_4

            data={
                'biologico':'INFLUENZA',
                'dosis':'4ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "7005":
            nombretabbio=T_INFLUENZA_5

            data={
                'biologico':'INFLUENZA',
                'dosis':'5ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "7006":
            nombretabbio=T_INFLUENZA_R1

            data={
                'biologico':'INFLUENZA',
                'dosis':'1er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "7007":
            nombretabbio=T_INFLUENZA_R2

            data={
                'biologico':'INFLUENZA',
                'dosis':'2do Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "7008":
            nombretabbio=T_INFLUENZA_R3

            data={
                'biologico':'INFLUENZA',
                'dosis':'3er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "8000":
            nombretabbio=T_COVID_U

            data={
                'biologico':'COVID',
                'dosis':'Unica',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "8001":
            nombretabbio=T_COVID_1

            data={
                'biologico':'COVID',
                'dosis':'1ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "8002":
            nombretabbio=T_COVID_2

            data={
                'biologico':'COVID',
                'dosis':'2da Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "8003":
            nombretabbio=T_COVID_3

            data={
                'biologico':'COVID',
                'dosis':'3ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "8004":
            nombretabbio=T_COVID_4

            data={
                'biologico':'COVID',
                'dosis':'4ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "8005":
            nombretabbio=T_COVID_5

            data={
                'biologico':'COVID',
                'dosis':'5ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "8006":
            nombretabbio=T_COVID_R1

            data={
                'biologico':'COVID',
                'dosis':'1er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "8007":
            nombretabbio=T_COVID_R2

            data={
                'biologico':'COVID',
                'dosis':'2do Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "8008":
            nombretabbio=T_COVID_R3

            data={
                'biologico':'COVID',
                'dosis':'3er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "9000":
            nombretabbio=T_HERPES_ZOSTER_U

            data={
                'biologico':'HERPES ZOSTER',
                'dosis':'Unica',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "9001":
            nombretabbio=T_HERPES_ZOSTER_1

            data={
                'biologico':'HERPES ZOSTER',
                'dosis':'1ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "9002":
            nombretabbio=T_HERPES_ZOSTER_2

            data={
                'biologico':'HERPES ZOSTER',
                'dosis':'2da Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "9003":
            nombretabbio=T_HERPES_ZOSTER_3

            data={
                'biologico':'HERPES ZOSTER',
                'dosis':'3ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "9004":
            nombretabbio=T_HERPES_ZOSTER_4

            data={
                'biologico':'HERPES ZOSTER',
                'dosis':'4ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "9005":
            nombretabbio=T_HERPES_ZOSTER_5

            data={
                'biologico':'HERPES ZOSTER',
                'dosis':'5ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "9006":
            nombretabbio=T_HERPES_ZOSTER_R1

            data={
                'biologico':'HERPES ZOSTER',
                'dosis':'1er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "9007":
            nombretabbio=T_HERPES_ZOSTER_R2

            data={
                'biologico':'HERPES ZOSTER',
                'dosis':'2do Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "9008":
            nombretabbio=T_HERPES_ZOSTER_R3

            data={
                'biologico':'HERPES ZOSTER',
                'dosis':'3er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "10000":
            nombretabbio=T_HEPATITIS_B_U

            data={
                'biologico':'HEPATITIS B',
                'dosis':'Unica',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "10001":
            nombretabbio=T_HEPATITIS_B_1

            data={
                'biologico':'HEPATITIS B',
                'dosis':'1ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "10002":
            nombretabbio=T_HEPATITIS_B_2

            data={
                'biologico':'HEPATITIS B',
                'dosis':'2da Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "10003":
            nombretabbio=T_HEPATITIS_B_3

            data={
                'biologico':'HEPATITIS B',
                'dosis':'3ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "10004":
            nombretabbio=T_HEPATITIS_B_4

            data={
                'biologico':'HEPATITIS B',
                'dosis':'4ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "10005":
            nombretabbio=T_HEPATITIS_B_5

            data={
                'biologico':'HEPATITIS B',
                'dosis':'5ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "10006":
            nombretabbio=T_HEPATITIS_B_R1

            data={
                'biologico':'HEPATITIS B',
                'dosis':'1er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "10007":
            nombretabbio=T_HEPATITIS_B_R2

            data={
                'biologico':'HEPATITIS B',
                'dosis':'2do Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "10008":
            nombretabbio=T_HEPATITIS_B_R3

            data={
                'biologico':'HEPATITIS B',
                'dosis':'3er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "11000":
            nombretabbio=T_ANTIRRABICA_U

            data={
                'biologico':'ANTIRRABICA',
                'dosis':'Unica',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "11001":
            nombretabbio=T_ANTIRRABICA_1

            data={
                'biologico':'ANTIRRABICA',
                'dosis':'1ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "11002":
            nombretabbio=T_ANTIRRABICA_2

            data={
                'biologico':'ANTIRRABICA',
                'dosis':'2da Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "11003":
            nombretabbio=T_ANTIRRABICA_3

            data={
                'biologico':'ANTIRRABICA',
                'dosis':'3ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }
        case "11004":
            nombretabbio=T_ANTIRRABICA_4

            data={
                'biologico':'ANTIRRABICA',
                'dosis':'4ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "11005":
            nombretabbio=T_ANTIRRABICA_5

            data={
                'biologico':'ANTIRRABICA',
                'dosis':'5ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "11006":
            nombretabbio=T_ANTIRRABICA_R1

            data={
                'biologico':'ANTIRRABICA',
                'dosis':'1er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "11007":
            nombretabbio=T_ANTIRRABICA_R2

            data={
                'biologico':'ANTIRRABICA',
                'dosis':'2do Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "11008":
            nombretabbio=T_ANTIRRABICA_R3

            data={
                'biologico':'ANTIRRABICA',
                'dosis':'3er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "12000":
            nombretabbio=T_VPH_U

            data={
                'biologico':'VPH',
                'dosis':'Unica',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "12001":
            nombretabbio=T_VPH_1

            data={
                'biologico':'VPH',
                'dosis':'1ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "12002":
            nombretabbio=T_VPH_2

            data={
                'biologico':'VPH',
                'dosis':'2da Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "12003":
            nombretabbio=T_VPH_3

            data={
                'biologico':'VPH',
                'dosis':'3ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "12004":
            nombretabbio=T_VPH_4

            data={
                'biologico':'VPH',
                'dosis':'4ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "12005":
            nombretabbio=T_VPH_5

            data={
                'biologico':'VPH',
                'dosis':'5ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "12006":
            nombretabbio=T_VPH_R1

            data={
                'biologico':'VPH',
                'dosis':'1er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "12007":
            nombretabbio=T_VPH_R2

            data={
                'biologico':'VPH',
                'dosis':'2do Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "12008":
            nombretabbio=T_VPH_R3

            data={
                'biologico':'VPH',
                'dosis':'3er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "13000":
            nombretabbio=T_HA_HB_U

            data={
                'biologico':'HA+HB',
                'dosis':'Unica',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "13001":
            nombretabbio=T_HA_HB_1

            data={
                'biologico':'HA+HB',
                'dosis':'1ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "13002":
            nombretabbio=T_HA_HB_2

            data={
                'biologico':'HA+HB',
                'dosis':'2da Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "13003":
            nombretabbio=T_HA_HB_3

            data={
                'biologico':'HA+HB',
                'dosis':'3ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "13004":
            nombretabbio=T_HA_HB_4

            data={
                'biologico':'HA+HB',
                'dosis':'4ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "13005":
            nombretabbio=T_HA_HB_5

            data={
                'biologico':'HA+HB',
                'dosis':'5ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "13006":
            nombretabbio=T_HA_HB_R1

            data={
                'biologico':'HA+HB',
                'dosis':'1er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "13007":
            nombretabbio=T_HA_HB_R2

            data={
                'biologico':'HA+HB',
                'dosis':'2do Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "13008":
            nombretabbio=T_HA_HB_R3

            data={
                'biologico':'HA+HB',
                'dosis':'3er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "14000":
            nombretabbio=T_TETANO_ANTITETANICA_U

            data={
                'biologico':'TETANO ANTITETANICA',
                'dosis':'Unica',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "14001":
            nombretabbio=T_TETANO_ANTITETANICA_1

            data={
                'biologico':'TETANO ANTITETANICA',
                'dosis':'1ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "14002":
            nombretabbio=T_TETANO_ANTITETANICA_2

            data={
                'biologico':'TETANO ANTITETANICA',
                'dosis':'2da Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "14003":
            nombretabbio=T_TETANO_ANTITETANICA_3

            data={
                'biologico':'TETANO ANTITETANICA',
                'dosis':'3ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "14004":
            nombretabbio=T_TETANO_ANTITETANICA_4

            data={
                'biologico':'TETANO ANTITETANICA',
                'dosis':'4ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "14005":
            nombretabbio=T_TETANO_ANTITETANICA_5

            data={
                'biologico':'TETANO ANTITETANICA',
                'dosis':'5ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "14006":
            nombretabbio=T_TETANO_ANTITETANICA_R1

            data={
                'biologico':'TETANO ANTITETANICA',
                'dosis':'1er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "14007":
            nombretabbio=T_TETANO_ANTITETANICA_R2

            data={
                'biologico':'TETANO ANTITETANICA',
                'dosis':'2do Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "14008":
            nombretabbio=T_TETANO_ANTITETANICA_R3

            data={
                'biologico':'TETANO ANTITETANICA',
                'dosis':'3er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "15000":
            nombretabbio=T_TETANO_DIFTERICO_U

            data={
                'biologico':'TETANO DIFTERICO',
                'dosis':'Unica',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "15001":
            nombretabbio=T_TETANO_DIFTERICO_1

            data={
                'biologico':'TETANO DIFTERICO',
                'dosis':'1ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "15002":
            nombretabbio=T_TETANO_DIFTERICO_2

            data={
                'biologico':'TETANO DIFTERICO',
                'dosis':'2da Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "15003":
            nombretabbio=T_TETANO_DIFTERICO_3

            data={
                'biologico':'TETANO DIFTERICO',
                'dosis':'3ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "15004":
            nombretabbio=T_TETANO_DIFTERICO_4

            data={
                'biologico':'TETANO DIFTERICO',
                'dosis':'4ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "15005":
            nombretabbio=T_TETANO_DIFTERICO_5

            data={
                'biologico':'TETANO DIFTERICO',
                'dosis':'5ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "15006":
            nombretabbio=T_TETANO_DIFTERICO_R1

            data={
                'biologico':'TETANO DIFTERICO',
                'dosis':'1er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "15007":
            nombretabbio=T_TETANO_DIFTERICO_R2

            data={
                'biologico':'TETANO DIFTERICO',
                'dosis':'2do Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "15008":
            nombretabbio=T_TETANO_DIFTERICO_R3

            data={
                'biologico':'TETANO DIFTERICO',
                'dosis':'3er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "16000":
            nombretabbio=T_FIEBRE_TIFOIDEA_U

            data={
                'biologico':'FIEBRE TIFOIDEA',
                'dosis':'Unica',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "16001":
            nombretabbio=T_FIEBRE_TIFOIDEA_1

            data={
                'biologico':'FIEBRE TIFOIDEA',
                'dosis':'1ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "16002":
            nombretabbio=T_FIEBRE_TIFOIDEA_2

            data={
                'biologico':'FIEBRE TIFOIDEA',
                'dosis':'2da Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "16003":
            nombretabbio=T_FIEBRE_TIFOIDEA_3

            data={
                'biologico':'FIEBRE TIFOIDEA',
                'dosis':'3ra Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "16004":
            nombretabbio=T_FIEBRE_TIFOIDEA_4

            data={
                'biologico':'FIEBRE TIFOIDEA',
                'dosis':'4ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "16005":
            nombretabbio=T_FIEBRE_TIFOIDEA_5

            data={
                'biologico':'FIEBRE TIFOIDEA',
                'dosis':'5ta Dosis',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "16006":
            nombretabbio=T_FIEBRE_TIFOIDEA_R1

            data={
                'biologico':'FIEBRE TIFOIDEA',
                'dosis':'1er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "16007":
            nombretabbio=T_FIEBRE_TIFOIDEA_R2

            data={
                'biologico':'FIEBRE TIFOIDEA',
                'dosis':'2do Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }

        case "16008":
            nombretabbio=T_FIEBRE_TIFOIDEA_R3

            data={
                'biologico':'FIEBRE TIFOIDEA',
                'dosis':'3er Refuerzo',
                'nombre': PacienteActual.nombre,
                'apellido': PacienteActual.apellido,
                'vacunador': request.user,
            }



    print(nombretabbio)

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
    
    
