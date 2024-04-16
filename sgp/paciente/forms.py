from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    
    class Meta:
        model = Paciente
        fields = '__all__'
        exclude = ('created', 'updated')