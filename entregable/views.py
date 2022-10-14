from django.shortcuts import render
from entregable.models import Familiar

def mostrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "entregable/familiares.html", {"lista_familiares": lista_familiares})

def saludar(request):
    return render(request, "entregable/saludar.html", {"nombre":"Saúl"})

def imc(request, peso, altura):
    imc = peso / ((altura*0.01)**2)
    return render(request, "entregable/imc.html", {"imc": imc})