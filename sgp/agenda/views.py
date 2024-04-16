from django.shortcuts import render, redirect

# Create your views here.
def mostrar(request):
    return render(request, "agenda/mostrar.html")