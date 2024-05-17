from django.db import models
from datetime import date

# Create your models here.

class VacunasPacientes(models.Model):

    DPT_ACELULAR= models.CharField(max_length=50, verbose_name='DPT')
    NEUMOCOCO_CONJUGADO= models.CharField(max_length=50, verbose_name='NEUMOCON')
    MENINGOCOCO= models.CharField(max_length=50, verbose_name='MENINGO')
    TRIPLE_VIRAL= models.CharField(max_length=50, verbose_name='TRIPLEVIRAL')
    VARICELA= models.CharField(max_length=50, verbose_name='VARICELA')
    HEPATITIS_A= models.CharField(max_length=50, verbose_name='HA')
    FIEBRE_AMARILLA= models.CharField(max_length=50, verbose_name='FIEBREAMARILLA')
    INFLUENZA= models.CharField(max_length=50, verbose_name='INFLUENZA')
    COVID= models.CharField(max_length=50, verbose_name='COVID')
    HERPES_ZOSTER= models.CharField(max_length=50, verbose_name='HERPES')
    HEPATITIS_B= models.CharField(max_length=50, verbose_name='HB')
    ANTIRRABICA= models.CharField(max_length=50, verbose_name='ANTIRRABICA')
    VPH= models.CharField(max_length=50, verbose_name='VPH')
    HA_HB= models.CharField(max_length=50, verbose_name='HAHB')
    TETANO_ANTITETANICA= models.CharField(max_length=50, verbose_name='TETANO')
    TETANO_DIFTERICO= models.CharField(max_length=50, verbose_name='TETANODIFTERICO')
    FIEBRE_TIFOIDEA= models.CharField(max_length=50, verbose_name='FIEBRETIFOIDEA')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
