from django.shortcuts import render, redirect, Http404, get_object_or_404
from .models import Tratamiento, Radiografia
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from paciente.models import Paciente
from .forms import TratamientoForm, RadiografiaForm
from django.contrib import messages


# Create your views here.

@login_required()
def listar_tratamientos(request):
    tratamientos = Tratamiento.objects.all().order_by('-created')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(tratamientos, 6)
        tratamientos = paginator.page(page)
    except:
        raise Http404
        
    data = {
        'tratamientos': tratamientos,
        'paginator': paginator
    }
    return render(request, 'tratamiento/listar_tratamientos.html', data)

@login_required()
def ver_tratamiento(request, id):
    #Ver un tratamiento especifico desde el listado gral.
    tratamiento = Tratamiento.objects.filter(id=id)
    id_tratamiento = tratamiento.values_list()[0][0]
    radiografias = Radiografia.objects.filter(tratamiento=id_tratamiento)
    data = {
        'tratamiento': tratamiento,
        'radiografias': radiografias
    }    
    return render(request, 'tratamiento/ver_tratamiento.html', data)

@login_required()
def paciente_tratamientos(request, id):
    #Recibe un ID del paciente, retorna todos sus tratamientos
    tratamientos = Tratamiento.objects.filter(paciente=id)
    paciente = Paciente.objects.get(id=id)
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(tratamientos, 6)
        tratamientos = paginator.page(page)
    except:
        raise Http404
    data = {
        'tratamientos': tratamientos,
        'paciente':paciente,
        'paginator': paginator
    }    
    return render(request, "tratamiento/paciente_tratamientos.html", data)

@login_required()
def paciente_radiografias(request, id):
    paciente = Paciente.objects.get(id=id)
    #Recibe un ID del paciente, retorna todas sus radiografías
    tratamientos = Tratamiento.objects.filter(paciente=id)
    
    lista = []
    id_tratamientos = []
    for t in tratamientos.values_list():
        id_tratamientos.append(t[0])
    for x in id_tratamientos:
        radiografias = Radiografia.objects.filter(tratamiento=x)
        lista.append(radiografias)
      
    data = {
        'lista': lista,
        'paciente': paciente,
    }
    return render(request, "tratamiento/paciente_radiografias.html", data)

@login_required()
def registrar_tratamiento(request):
    pacientes = Paciente.objects.all()
    data = {
        'pacientes': pacientes,
        'form': TratamientoForm()
    }    
    if request.method == 'POST':
        formulario = TratamientoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            #Completo el paciente
            formulario.instance.paciente = get_object_or_404(Paciente, id=request.POST['paciente'])
            formulario.save()
            messages.success(request, "Se guardaron los datos del tratamiento.")
            return redirect(to="/listar_tratamientos")
        data["form"] = formulario 
    return render(request, "tratamiento/registrar_tratamiento.html", data)

@login_required()
def guardar_radiografia_tratamiento(request):
    tratamientos = Tratamiento.objects.all()
    data = {
        'tratamientos': tratamientos,
        'form': RadiografiaForm()
    }
    if request.method == 'POST':               
        formulario = RadiografiaForm(request.POST, request.FILES)                
        if formulario.is_valid():
            formulario.instance.tratamiento = get_object_or_404(Tratamiento, id=request.POST['tratamiento'])
            formulario.save()
            messages.success(request, "Se guardo la radiografía.")
            return redirect(to="/listar_tratamientos")
        data["form"] = formulario    
    return render(request, "tratamiento/radiografiasTratamiento.html", data)