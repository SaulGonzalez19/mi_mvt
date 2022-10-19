from django.shortcuts import render
from entregable.models import Familiar
from entregable.forms import Buscar
from django.views import View

def mostrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "entregable/familiares.html", {"lista_familiares": lista_familiares})
    

def saludar(request):
    return render(request, "entregable/saludar.html", {"nombre":"Saúl"})

def imc(request, peso, altura):
    imc = peso / ((altura*0.01)**2)
    return render(request, "entregable/imc.html", {"imc": imc})

class BuscarFamiliar(View):

    form_class = Buscar
    template_name = 'entregable/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})

        return render(request, self.template_name, {"form": form})