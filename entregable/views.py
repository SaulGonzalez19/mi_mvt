from django.shortcuts import render

def saludar(request):
    return render(request, "entregable/saludar.html", {"nombre":"Saúl"})

def imc(request, peso, altura):
    imc = peso / (altura*100)**2
    return render(request, "entregable/imc.html", {"imc": imc})