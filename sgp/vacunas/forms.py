from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class DPT_ACELULAR_U(forms.ModelForm):
    
    class Meta:
        model = DPT_ACELULAR_U
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class DPT_ACELULAR_1(forms.ModelForm):
    
    class Meta:
        model = DPT_ACELULAR_1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class DPT_ACELULAR_2(forms.ModelForm):
    
    class Meta:
        model = DPT_ACELULAR_2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class DPT_ACELULAR_3(forms.ModelForm):
    
    class Meta:
        model = DPT_ACELULAR_3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class DPT_ACELULAR_4(forms.ModelForm):
    
    class Meta:
        model = DPT_ACELULAR_4
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class DPT_ACELULAR_5(forms.ModelForm):
    
    class Meta:
        model = DPT_ACELULAR_5
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class DPT_ACELULAR_R1(forms.ModelForm):
    
    class Meta:
        model = DPT_ACELULAR_R1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class DPT_ACELULAR_R2(forms.ModelForm):
    
    class Meta:
        model = DPT_ACELULAR_R2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class DPT_ACELULAR_R3(forms.ModelForm):
    
    class Meta:
        model = DPT_ACELULAR_R3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')


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

class MENINGOCOCO_U(forms.ModelForm):
    
    class Meta:
        model = MENINGOCOCO_U
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class MENINGOCOCO_1(forms.ModelForm):
    
    class Meta:
        model = MENINGOCOCO_1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class MENINGOCOCO_2(forms.ModelForm):
    
    class Meta:
        model = MENINGOCOCO_2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class MENINGOCOCO_3(forms.ModelForm):
    
    class Meta:
        model = MENINGOCOCO_3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')         

class MENINGOCOCO_4(forms.ModelForm):
    
    class Meta:
        model = MENINGOCOCO_4
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class MENINGOCOCO_5(forms.ModelForm):
    
    class Meta:
        model = MENINGOCOCO_5
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class MENINGOCOCO_R1(forms.ModelForm):
    
    class Meta:
        model = MENINGOCOCO_R1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class MENINGOCOCO_R2(forms.ModelForm):
    
    class Meta:
        model = MENINGOCOCO_R2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class MENINGOCOCO_R3(forms.ModelForm):
    
    class Meta:
        model = MENINGOCOCO_R3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class TRIPLE_VIRAL_U(forms.ModelForm):
    
    class Meta:
        model = TRIPLE_VIRAL_U
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class TRIPLE_VIRAL_1(forms.ModelForm):
    
    class Meta:
        model = TRIPLE_VIRAL_1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class TRIPLE_VIRAL_2(forms.ModelForm):
    
    class Meta:
        model = TRIPLE_VIRAL_2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class TRIPLE_VIRAL_3(forms.ModelForm):
    
    class Meta:
        model = TRIPLE_VIRAL_3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class TRIPLE_VIRAL_4(forms.ModelForm):
    
    class Meta:
        model = TRIPLE_VIRAL_4
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class TRIPLE_VIRAL_5(forms.ModelForm):
    
    class Meta:
        model = TRIPLE_VIRAL_5
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class TRIPLE_VIRAL_R1(forms.ModelForm):
    
    class Meta:
        model = TRIPLE_VIRAL_R1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class TRIPLE_VIRAL_R2(forms.ModelForm):
    
    class Meta:
        model = TRIPLE_VIRAL_R2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class TRIPLE_VIRAL_R3(forms.ModelForm):
    
    class Meta:
        model = TRIPLE_VIRAL_R3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class VARICELA_U(forms.ModelForm):
    
    class Meta:
        model = VARICELA_U
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class VARICELA_1(forms.ModelForm):
    
    class Meta:
        model = VARICELA_1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class VARICELA_2(forms.ModelForm):
    
    class Meta:
        model = VARICELA_2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class VARICELA_3(forms.ModelForm):
    
    class Meta:
        model = VARICELA_3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class VARICELA_4(forms.ModelForm):
    
    class Meta:
        model = VARICELA_4
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class VARICELA_5(forms.ModelForm):
    
    class Meta:
        model = VARICELA_5
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class VARICELA_R1(forms.ModelForm):
    
    class Meta:
        model = VARICELA_R1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class VARICELA_R2(forms.ModelForm):
    
    class Meta:
        model = VARICELA_R2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class VARICELA_R3(forms.ModelForm):
    
    class Meta:
        model = VARICELA_R3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HEPATITIS_A_U(forms.ModelForm):
    
    class Meta:
        model = HEPATITIS_A_U
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HEPATITIS_A_1(forms.ModelForm):
    
    class Meta:
        model = HEPATITIS_A_1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HEPATITIS_A_2(forms.ModelForm):
    
    class Meta:
        model = HEPATITIS_A_2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HEPATITIS_A_3(forms.ModelForm):
    
    class Meta:
        model = HEPATITIS_A_3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HEPATITIS_A_4(forms.ModelForm):
    
    class Meta:
        model = HEPATITIS_A_4
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HEPATITIS_A_5(forms.ModelForm):
    
    class Meta:
        model = HEPATITIS_A_5
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HEPATITIS_A_R1(forms.ModelForm):
    
    class Meta:
        model = HEPATITIS_A_R1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HEPATITIS_A_R2(forms.ModelForm):
    
    class Meta:
        model = HEPATITIS_A_R2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HEPATITIS_A_R3(forms.ModelForm):
    
    class Meta:
        model = HEPATITIS_A_R3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class FIEBRE_AMARILLA_U(forms.ModelForm):
    
    class Meta:
        model = FIEBRE_AMARILLA_U
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class FIEBRE_AMARILLA_1(forms.ModelForm):
    
    class Meta:
        model = FIEBRE_AMARILLA_1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class FIEBRE_AMARILLA_2(forms.ModelForm):
    
    class Meta:
        model = FIEBRE_AMARILLA_2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class FIEBRE_AMARILLA_3(forms.ModelForm):
    
    class Meta:
        model = FIEBRE_AMARILLA_3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class FIEBRE_AMARILLA_4(forms.ModelForm):
    
    class Meta:
        model = FIEBRE_AMARILLA_4
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class FIEBRE_AMARILLA_5(forms.ModelForm):
    
    class Meta:
        model = FIEBRE_AMARILLA_5
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class FIEBRE_AMARILLA_R1(forms.ModelForm):
    
    class Meta:
        model = FIEBRE_AMARILLA_R1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class FIEBRE_AMARILLA_R2(forms.ModelForm):
    
    class Meta:
        model = FIEBRE_AMARILLA_R2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class FIEBRE_AMARILLA_R3(forms.ModelForm):
    
    class Meta:
        model = FIEBRE_AMARILLA_R3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class INFLUENZA_U(forms.ModelForm):
    
    class Meta:
        model = INFLUENZA_U
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class INFLUENZA_1(forms.ModelForm):
    
    class Meta:
        model = INFLUENZA_1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class INFLUENZA_2(forms.ModelForm):
    
    class Meta:
        model = INFLUENZA_2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class INFLUENZA_3(forms.ModelForm):
    
    class Meta:
        model = INFLUENZA_3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class INFLUENZA_4(forms.ModelForm):
    
    class Meta:
        model = INFLUENZA_4
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class INFLUENZA_5(forms.ModelForm):
    
    class Meta:
        model = INFLUENZA_5
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class INFLUENZA_R1(forms.ModelForm):
    
    class Meta:
        model = INFLUENZA_R1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class INFLUENZA_R2(forms.ModelForm):
    
    class Meta:
        model = INFLUENZA_R2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class INFLUENZA_R3(forms.ModelForm):
    
    class Meta:
        model = INFLUENZA_R3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class COVID_U(forms.ModelForm):
    
    class Meta:
        model = COVID_U
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class COVID_1(forms.ModelForm):
    
    class Meta:
        model = COVID_1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class COVID_2(forms.ModelForm):
    
    class Meta:
        model = COVID_2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class COVID_3(forms.ModelForm):
    
    class Meta:
        model = COVID_3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class COVID_4(forms.ModelForm):
    
    class Meta:
        model = COVID_4
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class COVID_5(forms.ModelForm):
    
    class Meta:
        model = COVID_5
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class COVID_R1(forms.ModelForm):
    
    class Meta:
        model = COVID_R1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class COVID_R2(forms.ModelForm):
    
    class Meta:
        model = COVID_R2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class COVID_R3(forms.ModelForm):
    
    class Meta:
        model = COVID_R3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HERPES_ZOSTER_U(forms.ModelForm):
    
    class Meta:
        model = HERPES_ZOSTER_U
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HERPES_ZOSTER_1(forms.ModelForm):
    
    class Meta:
        model = HERPES_ZOSTER_1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HERPES_ZOSTER_2(forms.ModelForm):
    
    class Meta:
        model = HERPES_ZOSTER_2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HERPES_ZOSTER_3(forms.ModelForm):
    
    class Meta:
        model = HERPES_ZOSTER_3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HERPES_ZOSTER_4(forms.ModelForm):
    
    class Meta:
        model = HERPES_ZOSTER_4
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HERPES_ZOSTER_5(forms.ModelForm):
    
    class Meta:
        model = HERPES_ZOSTER_5
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HERPES_ZOSTER_R1(forms.ModelForm):
    
    class Meta:
        model = HERPES_ZOSTER_R1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HERPES_ZOSTER_R2(forms.ModelForm):
    
    class Meta:
        model = HERPES_ZOSTER_R2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HERPES_ZOSTER_R3(forms.ModelForm):
    
    class Meta:
        model = HERPES_ZOSTER_R3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HEPATITIS_B_U(forms.ModelForm):
    
    class Meta:
        model = HEPATITIS_B_U
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HEPATITIS_B_1(forms.ModelForm):
    
    class Meta:
        model = HEPATITIS_B_1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HEPATITIS_B_2(forms.ModelForm):
    
    class Meta:
        model = HEPATITIS_B_2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HEPATITIS_B_3(forms.ModelForm):
    
    class Meta:
        model = HEPATITIS_B_3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HEPATITIS_B_4(forms.ModelForm):
    
    class Meta:
        model = HEPATITIS_B_4
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HEPATITIS_B_5(forms.ModelForm):
    
    class Meta:
        model = HEPATITIS_B_5
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HEPATITIS_B_R1(forms.ModelForm):
    
    class Meta:
        model = HEPATITIS_B_R1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HEPATITIS_B_R2(forms.ModelForm):
    
    class Meta:
        model = HEPATITIS_B_R2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HEPATITIS_B_R3(forms.ModelForm):
    
    class Meta:
        model = HEPATITIS_B_R3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class ANTIRRABICA_U(forms.ModelForm):
    
    class Meta:
        model = ANTIRRABICA_U
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class ANTIRRABICA_1(forms.ModelForm):
    
    class Meta:
        model = ANTIRRABICA_1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class ANTIRRABICA_2(forms.ModelForm):
    
    class Meta:
        model = ANTIRRABICA_2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class ANTIRRABICA_3(forms.ModelForm):
    
    class Meta:
        model = ANTIRRABICA_3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class ANTIRRABICA_4(forms.ModelForm):
    
    class Meta:
        model = ANTIRRABICA_4
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class ANTIRRABICA_5(forms.ModelForm):
    
    class Meta:
        model = ANTIRRABICA_5
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class ANTIRRABICA_R1(forms.ModelForm):
    
    class Meta:
        model = ANTIRRABICA_R1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class ANTIRRABICA_R2(forms.ModelForm):
    
    class Meta:
        model = ANTIRRABICA_R2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class ANTIRRABICA_R3(forms.ModelForm):
    
    class Meta:
        model = ANTIRRABICA_R3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class VPH_U(forms.ModelForm):
    
    class Meta:
        model = VPH_U
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class VPH_1(forms.ModelForm):
    
    class Meta:
        model = VPH_1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class VPH_2(forms.ModelForm):
    
    class Meta:
        model = VPH_2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class VPH_3(forms.ModelForm):
    
    class Meta:
        model = VPH_3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class VPH_4(forms.ModelForm):
    
    class Meta:
        model = VPH_4
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class VPH_5(forms.ModelForm):
    
    class Meta:
        model = VPH_5
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class VPH_R1(forms.ModelForm):
    
    class Meta:
        model = VPH_R1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class VPH_R2(forms.ModelForm):
    
    class Meta:
        model = VPH_R2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class VPH_R3(forms.ModelForm):
    
    class Meta:
        model = VPH_R3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HA_HB_U(forms.ModelForm):
    
    class Meta:
        model = HA_HB_U
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HA_HB_1(forms.ModelForm):
    
    class Meta:
        model = HA_HB_1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HA_HB_2(forms.ModelForm):
    
    class Meta:
        model = HA_HB_2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HA_HB_3(forms.ModelForm):
    
    class Meta:
        model = HA_HB_3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HA_HB_4(forms.ModelForm):
    
    class Meta:
        model = HA_HB_4
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HA_HB_5(forms.ModelForm):
    
    class Meta:
        model = HA_HB_5
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HA_HB_R1(forms.ModelForm):
    
    class Meta:
        model = HA_HB_R1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HA_HB_R2(forms.ModelForm):
    
    class Meta:
        model = HA_HB_R2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class HA_HB_R3(forms.ModelForm):
    
    class Meta:
        model = HA_HB_R3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class TETANO_ANTITETANICA_U(forms.ModelForm):
    
    class Meta:
        model = TETANO_ANTITETANICA_U
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')

class TETANO_ANTITETANICA_1(forms.ModelForm):
    
    class Meta:
        model = TETANO_ANTITETANICA_1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')
class TETANO_ANTITETANICA_2(forms.ModelForm):
    
    class Meta:
        model = TETANO_ANTITETANICA_2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')      
class TETANO_ANTITETANICA_3(forms.ModelForm):
    
    class Meta:
        model = TETANO_ANTITETANICA_3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')      
class TETANO_ANTITETANICA_4(forms.ModelForm):
    
    class Meta:
        model = TETANO_ANTITETANICA_4
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')      
class TETANO_ANTITETANICA_5(forms.ModelForm):
    
    class Meta:
        model = TETANO_ANTITETANICA_5
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')      
class TETANO_ANTITETANICA_R1(forms.ModelForm):
    
    class Meta:
        model = TETANO_ANTITETANICA_R1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')     
class TETANO_ANTITETANICA_R2(forms.ModelForm):
    
    class Meta:
        model = TETANO_ANTITETANICA_R2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')     
class TETANO_ANTITETANICA_R3(forms.ModelForm):
    
    class Meta:
        model = TETANO_ANTITETANICA_R3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')      
class TETANO_DIFTERICO_U(forms.ModelForm):
    
    class Meta:
        model = TETANO_DIFTERICO_U
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')     
class TETANO_DIFTERICO_1(forms.ModelForm):
    
    class Meta:
        model = TETANO_DIFTERICO_1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')      
class TETANO_DIFTERICO_2(forms.ModelForm):
    
    class Meta:
        model = TETANO_DIFTERICO_2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')      
class TETANO_DIFTERICO_3(forms.ModelForm):
    
    class Meta:
        model = TETANO_DIFTERICO_3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')      
class TETANO_DIFTERICO_4(forms.ModelForm):
    
    class Meta:
        model = TETANO_DIFTERICO_4
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')      
class TETANO_DIFTERICO_5(forms.ModelForm):
    
    class Meta:
        model = TETANO_DIFTERICO_5
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')      
class TETANO_DIFTERICO_R1(forms.ModelForm):
    
    class Meta:
        model = TETANO_DIFTERICO_R1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')      
class TETANO_DIFTERICO_R2(forms.ModelForm):
    
    class Meta:
        model = TETANO_DIFTERICO_R2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')      
class TETANO_DIFTERICO_R3(forms.ModelForm):
    
    class Meta:
        model = TETANO_DIFTERICO_R3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')      
class FIEBRE_TIFOIDEA_U(forms.ModelForm):
    
    class Meta:
        model = FIEBRE_TIFOIDEA_U
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')      
class FIEBRE_TIFOIDEA_1(forms.ModelForm):
    
    class Meta:
        model = FIEBRE_TIFOIDEA_1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')      
class FIEBRE_TIFOIDEA_2(forms.ModelForm):
    
    class Meta:
        model = FIEBRE_TIFOIDEA_2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')      
class FIEBRE_TIFOIDEA_3(forms.ModelForm):
    
    class Meta:
        model = FIEBRE_TIFOIDEA_3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')      
class FIEBRE_TIFOIDEA_4(forms.ModelForm):
    
    class Meta:
        model = FIEBRE_TIFOIDEA_4
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')      
class FIEBRE_TIFOIDEA_5(forms.ModelForm):
    
    class Meta:
        model = FIEBRE_TIFOIDEA_5
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')      
class FIEBRE_TIFOIDEA_R1(forms.ModelForm):
    
    class Meta:
        model = FIEBRE_TIFOIDEA_R1
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')      
class FIEBRE_TIFOIDEA_R2(forms.ModelForm):
    
    class Meta:
        model = FIEBRE_TIFOIDEA_R2
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')      
class FIEBRE_TIFOIDEA_R3(forms.ModelForm):
    
    class Meta:
        model = FIEBRE_TIFOIDEA_R3
        fields = '__all__'
        exclude = ('created', 'updated', 'PACIENTE', 'NOMBREVACUNADOR')








































































































