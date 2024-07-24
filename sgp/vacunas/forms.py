from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import NEUMOCON

class NEUMOCOCO(forms.ModelForm):
    
    class Meta:
        model = NEUMOCON
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')