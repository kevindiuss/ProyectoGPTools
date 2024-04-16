from django import forms
from .models import Radiografia, Tratamiento

class TratamientoForm(forms.ModelForm):
    class Meta:
        model = Tratamiento
        fields = '__all__'
        exclude = ('created', 'updated')
        
class RadiografiaForm(forms.ModelForm):
    class Meta:
        model = Radiografia
        fields = '__all__'
        exclude = ('created', 'updated')