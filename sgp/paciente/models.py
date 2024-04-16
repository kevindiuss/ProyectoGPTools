from django.db import models
from ckeditor.fields import RichTextField
from datetime import date

# Create your models here.
class Paciente(models.Model):
    tipoId = models.CharField(max_length=50, verbose_name='tipoId')
    numDocumento = models.CharField(max_length=15, verbose_name='numDocumento')
    nombre = models.CharField(max_length=50, verbose_name='nombre')
    apellido = models.CharField(max_length=50, verbose_name='apellido')
    telefono = models.CharField(max_length=20, verbose_name='teléfono')
    telefonoDos = models.CharField(max_length=20, verbose_name='telefonoDos')
    email = models.EmailField(verbose_name='email')
    fecha_nacimiento = models.DateField(verbose_name='fechaNacimiento')    
    direccion = models.CharField(max_length=150, verbose_name='dirección')
    sexo = models.CharField(max_length=10)
    ocupacion = models.CharField(max_length=100)
    sangre = models.CharField(max_length=15)
    rh = models.CharField(max_length=20)
    grupoRiesgo = models.CharField(max_length=35)
    condicionSalud = models.CharField(max_length=50)
    regimen = models.CharField(max_length=20)
    aseguradora = models.CharField(max_length=50)
    tipoAfi = models.CharField(max_length=20)       
    observaciones = models.TextField(blank=True, null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return f'{self.apellido}, {self.nombre}'
    
    def calcularEdad(self):
        return date.today().year - self.fecha_nacimiento.year  
    
    class Meta:
        verbose_name = 'paciente'
        verbose_name_plural = 'pacientes'
        ordering = ['created']
