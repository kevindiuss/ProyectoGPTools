from django.db import models
from datetime import date
from paciente.models import Paciente

# Create your models here.

class VacunasPacientes(models.Model):

    PACIENTE=models.ForeignKey(Paciente, on_delete=models.CASCADE,primary_key=True)
    DPT_ACELULAR_U= models.CharField(max_length=50, verbose_name='DPTU', default="no")
    DPT_ACELULAR_1= models.CharField(max_length=50, verbose_name='DPT1', default="no")
    DPT_ACELULAR_2= models.CharField(max_length=50, verbose_name='DPT2', default="no")
    DPT_ACELULAR_3= models.CharField(max_length=50, verbose_name='DPT3', default="no")
    DPT_ACELULAR_4= models.CharField(max_length=50, verbose_name='DPT4', default="no")
    DPT_ACELULAR_5= models.CharField(max_length=50, verbose_name='DPT5', default="no")
    DPT_ACELULAR_R1= models.CharField(max_length=50, verbose_name='DPTR1', default="no")
    DPT_ACELULAR_R2= models.CharField(max_length=50, verbose_name='DPTR2', default="no")
    DPT_ACELULAR_R3= models.CharField(max_length=50, verbose_name='DPTR3', default="no")
    NEUMOCOCO_CONJUGADO_U= models.CharField(max_length=50, verbose_name='NEUMOCONU', default="no")
    NEUMOCOCO_CONJUGADO_1= models.CharField(max_length=50, verbose_name='NEUMOCON1', default="no")
    NEUMOCOCO_CONJUGADO_2= models.CharField(max_length=50, verbose_name='NEUMOCON2', default="no")
    NEUMOCOCO_CONJUGADO_3= models.CharField(max_length=50, verbose_name='NEUMOCON3', default="no")
    NEUMOCOCO_CONJUGADO_4= models.CharField(max_length=50, verbose_name='NEUMOCON4', default="no")
    NEUMOCOCO_CONJUGADO_5= models.CharField(max_length=50, verbose_name='NEUMOCON5', default="no")
    NEUMOCOCO_CONJUGADO_R1= models.CharField(max_length=50, verbose_name='NEUMOCONR1', default="no")
    NEUMOCOCO_CONJUGADO_R2= models.CharField(max_length=50, verbose_name='NEUMOCONR2', default="no")
    NEUMOCOCO_CONJUGADO_R3= models.CharField(max_length=50, verbose_name='NEUMOCONR3', default="no")
    MENINGOCOCO_U= models.CharField(max_length=50, verbose_name='MENINGOU', default="no")
    MENINGOCOCO_1= models.CharField(max_length=50, verbose_name='MENINGO1', default="no")
    MENINGOCOCO_2= models.CharField(max_length=50, verbose_name='MENINGO2', default="no")
    MENINGOCOCO_3= models.CharField(max_length=50, verbose_name='MENINGO3', default="no")
    MENINGOCOCO_4= models.CharField(max_length=50, verbose_name='MENINGO4', default="no")
    MENINGOCOCO_5= models.CharField(max_length=50, verbose_name='MENINGO5', default="no")
    MENINGOCOCO_R1= models.CharField(max_length=50, verbose_name='MENINGOR1', default="no")
    MENINGOCOCO_R2= models.CharField(max_length=50, verbose_name='MENINGOR2', default="no")
    MENINGOCOCO_R3= models.CharField(max_length=50, verbose_name='MENINGOR3', default="no")
    TRIPLE_VIRAL_U= models.CharField(max_length=50, verbose_name='TRIPLEVIRALU', default="no")
    TRIPLE_VIRAL_1= models.CharField(max_length=50, verbose_name='TRIPLEVIRAL1', default="no")
    TRIPLE_VIRAL_2= models.CharField(max_length=50, verbose_name='TRIPLEVIRAL2', default="no")
    TRIPLE_VIRAL_3= models.CharField(max_length=50, verbose_name='TRIPLEVIRAL3', default="no")
    TRIPLE_VIRAL_4= models.CharField(max_length=50, verbose_name='TRIPLEVIRAL4', default="no")
    TRIPLE_VIRAL_5= models.CharField(max_length=50, verbose_name='TRIPLEVIRAL5', default="no")
    TRIPLE_VIRAL_R1= models.CharField(max_length=50, verbose_name='TRIPLEVIRALR1', default="no")
    TRIPLE_VIRAL_R2= models.CharField(max_length=50, verbose_name='TRIPLEVIRALR2', default="no")
    TRIPLE_VIRAL_R3= models.CharField(max_length=50, verbose_name='TRIPLEVIRALR3', default="no")
    VARICELA_U= models.CharField(max_length=50, verbose_name='VARICELAU', default="no")
    VARICELA_1= models.CharField(max_length=50, verbose_name='VARICELA1', default="no")
    VARICELA_2= models.CharField(max_length=50, verbose_name='VARICELA2', default="no")
    VARICELA_3= models.CharField(max_length=50, verbose_name='VARICELA3', default="no")
    VARICELA_4= models.CharField(max_length=50, verbose_name='VARICELA4', default="no")
    VARICELA_5= models.CharField(max_length=50, verbose_name='VARICELA5', default="no")
    VARICELA_R1= models.CharField(max_length=50, verbose_name='VARICELAR1', default="no")
    VARICELA_R2= models.CharField(max_length=50, verbose_name='VARICELAR2', default="no")
    VARICELA_R3= models.CharField(max_length=50, verbose_name='VARICELAR3', default="no")
    HEPATITIS_A_U= models.CharField(max_length=50, verbose_name='HAU', default="no")
    HEPATITIS_A_1= models.CharField(max_length=50, verbose_name='HA1', default="no")
    HEPATITIS_A_2= models.CharField(max_length=50, verbose_name='HA2', default="no")
    HEPATITIS_A_3= models.CharField(max_length=50, verbose_name='HA3', default="no")
    HEPATITIS_A_4= models.CharField(max_length=50, verbose_name='HA4', default="no")
    HEPATITIS_A_5= models.CharField(max_length=50, verbose_name='HA5', default="no")
    HEPATITIS_A_R1= models.CharField(max_length=50, verbose_name='HAR1', default="no")
    HEPATITIS_A_R2= models.CharField(max_length=50, verbose_name='HAR2', default="no")
    HEPATITIS_A_R3= models.CharField(max_length=50, verbose_name='HAR3', default="no")
    FIEBRE_AMARILLA_U= models.CharField(max_length=50, verbose_name='FIEBREAMARILLAU', default="no")
    FIEBRE_AMARILLA_1= models.CharField(max_length=50, verbose_name='FIEBREAMARILLA1', default="no")
    FIEBRE_AMARILLA_2= models.CharField(max_length=50, verbose_name='FIEBREAMARILLA2', default="no")
    FIEBRE_AMARILLA_3= models.CharField(max_length=50, verbose_name='FIEBREAMARILLA3', default="no")
    FIEBRE_AMARILLA_4= models.CharField(max_length=50, verbose_name='FIEBREAMARILLA4', default="no")
    FIEBRE_AMARILLA_5= models.CharField(max_length=50, verbose_name='FIEBREAMARILLA5', default="no")
    FIEBRE_AMARILLA_R1= models.CharField(max_length=50, verbose_name='FIEBREAMARILLAR1', default="no")
    FIEBRE_AMARILLA_R2= models.CharField(max_length=50, verbose_name='FIEBREAMARILLAR2', default="no")
    FIEBRE_AMARILLA_R3= models.CharField(max_length=50, verbose_name='FIEBREAMARILLAR3', default="no")
    INFLUENZA_U= models.CharField(max_length=50, verbose_name='INFLUENZAU', default="no")
    INFLUENZA_1= models.CharField(max_length=50, verbose_name='INFLUENZA1', default="no")
    INFLUENZA_2= models.CharField(max_length=50, verbose_name='INFLUENZA2', default="no")
    INFLUENZA_3= models.CharField(max_length=50, verbose_name='INFLUENZA3', default="no")
    INFLUENZA_4= models.CharField(max_length=50, verbose_name='INFLUENZA4', default="no")
    INFLUENZA_5= models.CharField(max_length=50, verbose_name='INFLUENZA5', default="no")
    INFLUENZA_R1= models.CharField(max_length=50, verbose_name='INFLUENZAR1', default="no")
    INFLUENZA_R2= models.CharField(max_length=50, verbose_name='INFLUENZAR2', default="no")
    INFLUENZA_R3= models.CharField(max_length=50, verbose_name='INFLUENZAR3', default="no")
    COVID_U= models.CharField(max_length=50, verbose_name='COVIDU', default="no")
    COVID_1= models.CharField(max_length=50, verbose_name='COVID1', default="no")
    COVID_2= models.CharField(max_length=50, verbose_name='COVID2', default="no")
    COVID_3= models.CharField(max_length=50, verbose_name='COVID3', default="no")
    COVID_4= models.CharField(max_length=50, verbose_name='COVID4', default="no")
    COVID_5= models.CharField(max_length=50, verbose_name='COVID5', default="no")
    COVID_R1= models.CharField(max_length=50, verbose_name='COVIDR1', default="no")
    COVID_R2= models.CharField(max_length=50, verbose_name='COVIDR2', default="no")
    COVID_R3= models.CharField(max_length=50, verbose_name='COVIDR3', default="no")
    HERPES_ZOSTER_U= models.CharField(max_length=50, verbose_name='HERPESU', default="no")
    HERPES_ZOSTER_1= models.CharField(max_length=50, verbose_name='HERPES1', default="no")
    HERPES_ZOSTER_2= models.CharField(max_length=50, verbose_name='HERPES2', default="no")
    HERPES_ZOSTER_3= models.CharField(max_length=50, verbose_name='HERPES3', default="no")
    HERPES_ZOSTER_4= models.CharField(max_length=50, verbose_name='HERPES4', default="no")
    HERPES_ZOSTER_5= models.CharField(max_length=50, verbose_name='HERPES5', default="no")
    HERPES_ZOSTER_R1= models.CharField(max_length=50, verbose_name='HERPESR1', default="no")
    HERPES_ZOSTER_R2= models.CharField(max_length=50, verbose_name='HERPESR2', default="no")
    HERPES_ZOSTER_R3= models.CharField(max_length=50, verbose_name='HERPESR3', default="no")
    HEPATITIS_B_U= models.CharField(max_length=50, verbose_name='HBU', default="no")
    HEPATITIS_B_1= models.CharField(max_length=50, verbose_name='HB1', default="no")
    HEPATITIS_B_2= models.CharField(max_length=50, verbose_name='HB2', default="no")
    HEPATITIS_B_3= models.CharField(max_length=50, verbose_name='HB3', default="no")
    HEPATITIS_B_4= models.CharField(max_length=50, verbose_name='HB4', default="no")
    HEPATITIS_B_5= models.CharField(max_length=50, verbose_name='HB5', default="no")
    HEPATITIS_B_R1= models.CharField(max_length=50, verbose_name='HBR1', default="no")
    HEPATITIS_B_R2= models.CharField(max_length=50, verbose_name='HBR2', default="no")
    HEPATITIS_B_R3= models.CharField(max_length=50, verbose_name='HBR3', default="no")
    ANTIRRABICA_U= models.CharField(max_length=50, verbose_name='ANTIRRABICAU', default="no")
    ANTIRRABICA_1= models.CharField(max_length=50, verbose_name='ANTIRRABICA1', default="no")
    ANTIRRABICA_2= models.CharField(max_length=50, verbose_name='ANTIRRABICA2', default="no")
    ANTIRRABICA_3= models.CharField(max_length=50, verbose_name='ANTIRRABICA3', default="no")
    ANTIRRABICA_4= models.CharField(max_length=50, verbose_name='ANTIRRABICA4', default="no")
    ANTIRRABICA_5= models.CharField(max_length=50, verbose_name='ANTIRRABICA5', default="no")
    ANTIRRABICA_R1= models.CharField(max_length=50, verbose_name='ANTIRRABICAR1', default="no")
    ANTIRRABICA_R2= models.CharField(max_length=50, verbose_name='ANTIRRABICAR2', default="no")
    ANTIRRABICA_R3= models.CharField(max_length=50, verbose_name='ANTIRRABICAR3', default="no")
    VPH_U= models.CharField(max_length=50, verbose_name='VPHU', default="no")
    VPH_1= models.CharField(max_length=50, verbose_name='VPH1', default="no")
    VPH_2= models.CharField(max_length=50, verbose_name='VPH2', default="no")
    VPH_3= models.CharField(max_length=50, verbose_name='VPH3', default="no")
    VPH_4= models.CharField(max_length=50, verbose_name='VPH4', default="no")
    VPH_5= models.CharField(max_length=50, verbose_name='VPH5', default="no")
    VPH_R1= models.CharField(max_length=50, verbose_name='VPHR1', default="no")
    VPH_R2= models.CharField(max_length=50, verbose_name='VPHR2', default="no")
    VPH_R3= models.CharField(max_length=50, verbose_name='VPHR3', default="no")
    HA_HB_U= models.CharField(max_length=50, verbose_name='HAHBU', default="no")
    HA_HB_1= models.CharField(max_length=50, verbose_name='HAHB1', default="no")
    HA_HB_2= models.CharField(max_length=50, verbose_name='HAHB2', default="no")
    HA_HB_3= models.CharField(max_length=50, verbose_name='HAHB3', default="no")
    HA_HB_4= models.CharField(max_length=50, verbose_name='HAHB4', default="no")
    HA_HB_5= models.CharField(max_length=50, verbose_name='HAHB5', default="no")
    HA_HB_R1= models.CharField(max_length=50, verbose_name='HAHBR1', default="no")
    HA_HB_R2= models.CharField(max_length=50, verbose_name='HAHBR2', default="no")
    HA_HB_R3= models.CharField(max_length=50, verbose_name='HAHBR3', default="no")
    TETANO_ANTITETANICA_U= models.CharField(max_length=50, verbose_name='TETANOU', default="no")
    TETANO_ANTITETANICA_1= models.CharField(max_length=50, verbose_name='TETANO1', default="no")
    TETANO_ANTITETANICA_2= models.CharField(max_length=50, verbose_name='TETANO2', default="no")
    TETANO_ANTITETANICA_3= models.CharField(max_length=50, verbose_name='TETANO3', default="no")
    TETANO_ANTITETANICA_4= models.CharField(max_length=50, verbose_name='TETANO4', default="no")
    TETANO_ANTITETANICA_5= models.CharField(max_length=50, verbose_name='TETANO5', default="no")
    TETANO_ANTITETANICA_R1= models.CharField(max_length=50, verbose_name='TETANOR1', default="no")
    TETANO_ANTITETANICA_R2= models.CharField(max_length=50, verbose_name='TETANOR2', default="no")
    TETANO_ANTITETANICA_R3= models.CharField(max_length=50, verbose_name='TETANOR3', default="no")
    TETANO_DIFTERICO_U= models.CharField(max_length=50, verbose_name='TETANODIFTERICOU', default="no")
    TETANO_DIFTERICO_1= models.CharField(max_length=50, verbose_name='TETANODIFTERICO1', default="no")
    TETANO_DIFTERICO_2= models.CharField(max_length=50, verbose_name='TETANODIFTERICO2', default="no")
    TETANO_DIFTERICO_3= models.CharField(max_length=50, verbose_name='TETANODIFTERICO3', default="no")
    TETANO_DIFTERICO_4= models.CharField(max_length=50, verbose_name='TETANODIFTERICO4', default="no")
    TETANO_DIFTERICO_5= models.CharField(max_length=50, verbose_name='TETANODIFTERICO5', default="no")
    TETANO_DIFTERICO_R1= models.CharField(max_length=50, verbose_name='TETANODIFTERICOR1', default="no")
    TETANO_DIFTERICO_R2= models.CharField(max_length=50, verbose_name='TETANODIFTERICOR2', default="no")
    TETANO_DIFTERICO_R3= models.CharField(max_length=50, verbose_name='TETANODIFTERICOR3', default="no")
    FIEBRE_TIFOIDEA_U= models.CharField(max_length=50, verbose_name='FIEBRETIFOIDEAU', default="no")
    FIEBRE_TIFOIDEA_1= models.CharField(max_length=50, verbose_name='FIEBRETIFOIDEA1', default="no")
    FIEBRE_TIFOIDEA_2= models.CharField(max_length=50, verbose_name='FIEBRETIFOIDEA2', default="no")
    FIEBRE_TIFOIDEA_3= models.CharField(max_length=50, verbose_name='FIEBRETIFOIDEA3', default="no")
    FIEBRE_TIFOIDEA_4= models.CharField(max_length=50, verbose_name='FIEBRETIFOIDEA4', default="no")
    FIEBRE_TIFOIDEA_5= models.CharField(max_length=50, verbose_name='FIEBRETIFOIDEA5', default="no")
    FIEBRE_TIFOIDEA_R1= models.CharField(max_length=50, verbose_name='FIEBRETIFOIDEAR1', default="no")
    FIEBRE_TIFOIDEA_R2= models.CharField(max_length=50, verbose_name='FIEBRETIFOIDEAR2', default="no")
    FIEBRE_TIFOIDEA_R3= models.CharField(max_length=50, verbose_name='FIEBRETIFOIDEAR3', default="no")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Datoscomunvacun(models.Model):
    PACIENTE=models.ForeignKey(Paciente, on_delete=models.CASCADE,primary_key=True)
    LABORATORIO=models.CharField(max_length=25, verbose_name='labo')
    LOTE=models.CharField(max_length=20, verbose_name='lote')
    FECHAVENVACU=models.DateTimeField(verbose_name='fechavenvacun')    
    TACTIVAVACU=models.CharField(max_length=25, verbose_name='tacticavacun')
    FECHAAPLI=models.DateTimeField(verbose_name='fechaaplica')
    FECHAPROX=models.DateTimeField(verbose_name='fechaproxivacun')
    EMPRESA=models.CharField(max_length=30, verbose_name='nombrempresa')
    CONDICIONUSUARIA=models.CharField(max_length=30,verbose_name='condicionusuario')
    NOMBREVACUNADOR=models.CharField(max_length=30,verbose_name='nombrevacunadora')
    NUMFACTURA=models.CharField(max_length=30, verbose_name='numfactu')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class DPT_ACELULAR_U(Datoscomunvacun): 
    pass
class DPT_ACELULAR_1(Datoscomunvacun): 
    pass
class DPT_ACELULAR_2(Datoscomunvacun): 
    pass
class DPT_ACELULAR_3(Datoscomunvacun): 
    pass
class DPT_ACELULAR_4(Datoscomunvacun): 
    pass
class DPT_ACELULAR_5(Datoscomunvacun): 
    pass
class DPT_ACELULAR_R1(Datoscomunvacun): 
    pass
class DPT_ACELULAR_R2(Datoscomunvacun): 
    pass
class DPT_ACELULAR_R3(Datoscomunvacun): 
    pass

class NEUMOCON(Datoscomunvacun):
    pass
class NEUMOCON1(Datoscomunvacun):
    pass
class NEUMOCON2(Datoscomunvacun):
    pass 
class NEUMOCON3(Datoscomunvacun):
    pass
class NEUMOCON4(Datoscomunvacun):
    pass
class NEUMOCON5(Datoscomunvacun):
    pass
class NEUMOCONR1(Datoscomunvacun):
    pass
class NEUMOCONR2(Datoscomunvacun):
    pass
class NEUMOCONR3(Datoscomunvacun):
    pass

class MENINGOCOCO_U(Datoscomunvacun):
    pass
class MENINGOCOCO_1(Datoscomunvacun):
    pass
class MENINGOCOCO_2(Datoscomunvacun):
    pass
class MENINGOCOCO_3(Datoscomunvacun):
    pass
class MENINGOCOCO_4(Datoscomunvacun):
    pass
class MENINGOCOCO_5(Datoscomunvacun):
    pass
class MENINGOCOCO_R1(Datoscomunvacun):
    pass
class MENINGOCOCO_R2(Datoscomunvacun):
    pass
class MENINGOCOCO_R3(Datoscomunvacun):
    pass

class TRIPLE_VIRAL_U(Datoscomunvacun):
    pass
class TRIPLE_VIRAL_1(Datoscomunvacun):
    pass
class TRIPLE_VIRAL_2(Datoscomunvacun):
    pass
class TRIPLE_VIRAL_3(Datoscomunvacun):
    pass
class TRIPLE_VIRAL_4(Datoscomunvacun):
    pass
class TRIPLE_VIRAL_5(Datoscomunvacun):
    pass
class TRIPLE_VIRAL_R1(Datoscomunvacun):
    pass
class TRIPLE_VIRAL_R2(Datoscomunvacun):
    pass
class TRIPLE_VIRAL_R3(Datoscomunvacun):
    pass

class VARICELA_U(Datoscomunvacun):
    pass
class VARICELA_1(Datoscomunvacun):
    pass
class VARICELA_2(Datoscomunvacun):
    pass
class VARICELA_3(Datoscomunvacun):
    pass
class VARICELA_4(Datoscomunvacun):
    pass
class VARICELA_5(Datoscomunvacun):
    pass
class VARICELA_R1(Datoscomunvacun):
    pass
class VARICELA_R2(Datoscomunvacun):
    pass
class VARICELA_R3(Datoscomunvacun):
    pass

class HEPATITIS_A_U(Datoscomunvacun):
    pass
class HEPATITIS_A_1(Datoscomunvacun):
    pass
class HEPATITIS_A_2(Datoscomunvacun):
    pass
class HEPATITIS_A_3(Datoscomunvacun):
    pass
class HEPATITIS_A_4(Datoscomunvacun):
    pass
class HEPATITIS_A_5(Datoscomunvacun):
    pass
class HEPATITIS_A_R1(Datoscomunvacun):
    pass
class HEPATITIS_A_R2(Datoscomunvacun):
    pass
class HEPATITIS_A_R3(Datoscomunvacun):
    pass

class FIEBRE_AMARILLA_U(Datoscomunvacun):
    pass
class FIEBRE_AMARILLA_1(Datoscomunvacun):
    pass
class FIEBRE_AMARILLA_2(Datoscomunvacun):
    pass
class FIEBRE_AMARILLA_3(Datoscomunvacun):
    pass
class FIEBRE_AMARILLA_4(Datoscomunvacun):
    pass
class FIEBRE_AMARILLA_5(Datoscomunvacun):
    pass
class FIEBRE_AMARILLA_R1(Datoscomunvacun):
    pass
class FIEBRE_AMARILLA_R2(Datoscomunvacun):
    pass
class FIEBRE_AMARILLA_R3(Datoscomunvacun):
    pass

class INFLUENZA_U(Datoscomunvacun):
    pass
class INFLUENZA_1(Datoscomunvacun):
    pass
class INFLUENZA_2(Datoscomunvacun):
    pass
class INFLUENZA_3(Datoscomunvacun):
    pass
class INFLUENZA_4(Datoscomunvacun):
    pass
class INFLUENZA_5(Datoscomunvacun):
    pass
class INFLUENZA_R1(Datoscomunvacun):
    pass
class INFLUENZA_R2(Datoscomunvacun):
    pass
class INFLUENZA_R3(Datoscomunvacun):
    pass

class COVID_U(Datoscomunvacun):
    pass
class COVID_1(Datoscomunvacun):
    pass
class COVID_2(Datoscomunvacun):
    pass
class COVID_3(Datoscomunvacun):
    pass
class COVID_4(Datoscomunvacun):
    pass
class COVID_5(Datoscomunvacun):
    pass
class COVID_R1(Datoscomunvacun):
    pass
class COVID_R2(Datoscomunvacun):
    pass
class COVID_R3(Datoscomunvacun):
    pass

class HERPES_ZOSTER_U(Datoscomunvacun):
    pass
class HERPES_ZOSTER_1(Datoscomunvacun):
    pass
class HERPES_ZOSTER_2(Datoscomunvacun):
    pass
class HERPES_ZOSTER_3(Datoscomunvacun):
    pass
class HERPES_ZOSTER_4(Datoscomunvacun):
    pass
class HERPES_ZOSTER_5(Datoscomunvacun):
    pass
class HERPES_ZOSTER_R1(Datoscomunvacun):
    pass
class HERPES_ZOSTER_R2(Datoscomunvacun):
    pass
class HERPES_ZOSTER_R3(Datoscomunvacun):
    pass

class HEPATITIS_B_U(Datoscomunvacun):
    pass
class HEPATITIS_B_1(Datoscomunvacun):
    pass
class HEPATITIS_B_2(Datoscomunvacun):
    pass
class HEPATITIS_B_3(Datoscomunvacun):
    pass
class HEPATITIS_B_4(Datoscomunvacun):
    pass
class HEPATITIS_B_5(Datoscomunvacun):
    pass
class HEPATITIS_B_R1(Datoscomunvacun):
    pass
class HEPATITIS_B_R2(Datoscomunvacun):
    pass
class HEPATITIS_B_R3(Datoscomunvacun):
    pass

class ANTIRRABICA_U(Datoscomunvacun):
    pass
class ANTIRRABICA_1(Datoscomunvacun):
    pass
class ANTIRRABICA_2(Datoscomunvacun):
    pass
class ANTIRRABICA_3(Datoscomunvacun):
    pass
class ANTIRRABICA_4(Datoscomunvacun):
    pass
class ANTIRRABICA_5(Datoscomunvacun):
    pass
class ANTIRRABICA_R1(Datoscomunvacun):
    pass
class ANTIRRABICA_R2(Datoscomunvacun):
    pass
class ANTIRRABICA_R3(Datoscomunvacun):
    pass

class VPH_U(Datoscomunvacun):
    pass
class VPH_1(Datoscomunvacun):
    pass
class VPH_2(Datoscomunvacun):
    pass
class VPH_3(Datoscomunvacun):
    pass
class VPH_4(Datoscomunvacun):
    pass
class VPH_5(Datoscomunvacun):
    pass
class VPH_R1(Datoscomunvacun):
    pass
class VPH_R2(Datoscomunvacun):
    pass
class VPH_R3(Datoscomunvacun):
    pass

class HA_HB_U(Datoscomunvacun):
    pass
class HA_HB_1(Datoscomunvacun):
    pass
class HA_HB_2(Datoscomunvacun):
    pass
class HA_HB_3(Datoscomunvacun):
    pass
class HA_HB_4(Datoscomunvacun):
    pass
class HA_HB_5(Datoscomunvacun):
    pass
class HA_HB_R1(Datoscomunvacun):
    pass
class HA_HB_R2(Datoscomunvacun):
    pass
class HA_HB_R3(Datoscomunvacun):
    pass

class TETANO_ANTITETANICA_U(Datoscomunvacun):
    pass
class TETANO_ANTITETANICA_1(Datoscomunvacun):
    pass
class TETANO_ANTITETANICA_2(Datoscomunvacun):
    pass
class TETANO_ANTITETANICA_3(Datoscomunvacun):
    pass
class TETANO_ANTITETANICA_4(Datoscomunvacun):
    pass
class TETANO_ANTITETANICA_5(Datoscomunvacun):
    pass
class TETANO_ANTITETANICA_R1(Datoscomunvacun):
    pass
class TETANO_ANTITETANICA_R2(Datoscomunvacun):
    pass
class TETANO_ANTITETANICA_R3(Datoscomunvacun):
    pass


class TETANO_DIFTERICO_U(Datoscomunvacun):
    pass
class TETANO_DIFTERICO_1(Datoscomunvacun):
    pass
class TETANO_DIFTERICO_2(Datoscomunvacun):
    pass
class TETANO_DIFTERICO_3(Datoscomunvacun):
    pass
class TETANO_DIFTERICO_4(Datoscomunvacun):
    pass
class TETANO_DIFTERICO_5(Datoscomunvacun):
    pass
class TETANO_DIFTERICO_R1(Datoscomunvacun):
    pass
class TETANO_DIFTERICO_R2(Datoscomunvacun):
    pass
class TETANO_DIFTERICO_R3(Datoscomunvacun):
    pass

class FIEBRE_TIFOIDEA_U(Datoscomunvacun):
    pass
class FIEBRE_TIFOIDEA_1(Datoscomunvacun):
    pass
class FIEBRE_TIFOIDEA_2(Datoscomunvacun):
    pass
class FIEBRE_TIFOIDEA_3(Datoscomunvacun):
    pass
class FIEBRE_TIFOIDEA_4(Datoscomunvacun):
    pass
class FIEBRE_TIFOIDEA_5(Datoscomunvacun):
    pass
class FIEBRE_TIFOIDEA_R1(Datoscomunvacun):
    pass
class FIEBRE_TIFOIDEA_R2(Datoscomunvacun):
    pass
class FIEBRE_TIFOIDEA_R3(Datoscomunvacun):
    pass








# class MENINGO(models.Model):
#     PACIENTE=models.ForeignKey(Paciente, on_delete=models.CASCADE,primary_key=True)
# class TRIPLEVI(models.Model):
#     PACIENTE=models.ForeignKey(Paciente, on_delete=models.CASCADE,primary_key=True)
# class VARICELA(models.Model):
#     PACIENTE=models.ForeignKey(Paciente, on_delete=models.CASCADE,primary_key=True)
# class HA(models.Model):
#     PACIENTE=models.ForeignKey(Paciente, on_delete=models.CASCADE,primary_key=True)
# class FIEAMA(models.Model):
#     PACIENTE=models.ForeignKey(Paciente, on_delete=models.CASCADE,primary_key=True)
# class INFLU(models.Model):
#     PACIENTE=models.ForeignKey(Paciente, on_delete=models.CASCADE,primary_key=True)
# class COVID(models.Model):
#     PACIENTE=models.ForeignKey(Paciente, on_delete=models.CASCADE,primary_key=True)
# class HERPES(models.Model):
#     PACIENTE=models.ForeignKey(Paciente, on_delete=models.CASCADE,primary_key=True)
# class HB(models.Model):
#     PACIENTE=models.ForeignKey(Paciente, on_delete=models.CASCADE,primary_key=True)
# class ANTIRRA(models.Model):
#     PACIENTE=models.ForeignKey(Paciente, on_delete=models.CASCADE,primary_key=True)
# class VPH(models.Model):
#     PACIENTE=models.ForeignKey(Paciente, on_delete=models.CASCADE,primary_key=True)
# class HAHB(models.Model):
#     PACIENTE=models.ForeignKey(Paciente, on_delete=models.CASCADE,primary_key=True)
# class TETANAN(models.Model):
#     PACIENTE=models.ForeignKey(Paciente, on_delete=models.CASCADE,primary_key=True)
# class TETADIFT(models.Model):
#     PACIENTE=models.ForeignKey(Paciente, on_delete=models.CASCADE,primary_key=True)
# class FIEBTIFO(models.Model):
#     PACIENTE=models.ForeignKey(Paciente, on_delete=models.CASCADE,primary_key=True)