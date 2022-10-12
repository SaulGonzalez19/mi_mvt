from django.shortcuts import render

def saludar(request):
    return render(request, "entregable/saludar.html", {"nombre":"Saúl"})