from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class NEUMOCOCO(forms.ModelForm):
    
    class Meta:
        model = NEUMOCON
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class NEUMOCOCO1(forms.ModelForm):
    
    class Meta:
        model = NEUMOCON1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class NEUMOCOCO2(forms.ModelForm):
    
    class Meta:
        model = NEUMOCON2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class NEUMOCOCO3(forms.ModelForm):
    
    class Meta:
        model = NEUMOCON3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class NEUMOCOCO4(forms.ModelForm):
    
    class Meta:
        model = NEUMOCON4
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class NEUMOCOCO5(forms.ModelForm):
    
    class Meta:
        model = NEUMOCON5
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class NEUMOCOCOR1(forms.ModelForm):
    
    class Meta:
        model = NEUMOCONR1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class NEUMOCOCOR2(forms.ModelForm):
    
    class Meta:
        model = NEUMOCONR2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class NEUMOCOCOR3(forms.ModelForm):
    
    class Meta:
        model = NEUMOCONR3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')