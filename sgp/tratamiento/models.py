from django.db import models
from paciente.models import Paciente

# Create your models here.

class Tratamiento(models.Model):
    #Paciente que recibio el tratamiento
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    pieza = models.CharField(max_length=50)
    descripcion = models.TextField()      
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Tratamiento"
        verbose_name_plural = "Tratamientos"
        ordering = ["created"]
            
    def __str__(self):
        return f'{self.paciente}'

class Radiografia(models.Model):    
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='radiografias/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return f'ID: {self.id}'
