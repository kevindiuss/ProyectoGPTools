from django.shortcuts import render, redirect

# Create your views here.
def listar_presupuestos(request):
    return render(request, 'presupuesto/listar_presupuestos.html')