from django.db import models
from datetime import date
from paciente.models import Paciente

# Create your models here.

class VacunasPacientes(models.Model):

    PACIENTE=models.ForeignKey(Paciente, on_delete=models.CASCADE,primary_key=True)
    DPT_ACELULAR= models.CharField(max_length=50, verbose_name='DPT', default="no")
    NEUMOCOCO_CONJUGADO= models.CharField(max_length=50, verbose_name='NEUMOCON', default="no")
    MENINGOCOCO= models.CharField(max_length=50, verbose_name='MENINGO', default="no")
    TRIPLE_VIRAL= models.CharField(max_length=50, verbose_name='TRIPLEVIRAL', default="no")
    VARICELA= models.CharField(max_length=50, verbose_name='VARICELA', default="no")
    HEPATITIS_A= models.CharField(max_length=50, verbose_name='HA', default="no")
    FIEBRE_AMARILLA= models.CharField(max_length=50, verbose_name='FIEBREAMARILLA', default="no")
    INFLUENZA= models.CharField(max_length=50, verbose_name='INFLUENZA', default="no")
    COVID= models.CharField(max_length=50, verbose_name='COVID', default="no")
    HERPES_ZOSTER= models.CharField(max_length=50, verbose_name='HERPES', default="no")
    HEPATITIS_B= models.CharField(max_length=50, verbose_name='HB', default="no")
    ANTIRRABICA= models.CharField(max_length=50, verbose_name='ANTIRRABICA', default="no")
    VPH= models.CharField(max_length=50, verbose_name='VPH', default="no")
    HA_HB= models.CharField(max_length=50, verbose_name='HAHB', default="no")
    TETANO_ANTITETANICA= models.CharField(max_length=50, verbose_name='TETANO', default="no")
    TETANO_DIFTERICO= models.CharField(max_length=50, verbose_name='TETANODIFTERICO', default="no")
    FIEBRE_TIFOIDEA= models.CharField(max_length=50, verbose_name='FIEBRETIFOIDEA', default="no")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

# class DPTA(models.Model):

#     PACIENTE=models.ForeignKey(Paciente, on_delete=models.CASCADE,primary_key=True)

class NEUMOCON(models.Model):
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