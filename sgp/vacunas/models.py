from django.db import models
from datetime import date
from paciente.models import Paciente

# Create your models here.

class VacunasPacientes(models.Model):

    PACIENTE=models.OneToOneField(Paciente, on_delete=models.CASCADE,primary_key=True)
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
