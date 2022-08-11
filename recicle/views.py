
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .formu import RecicleForm #del formulario
from .models import Recicle

#////////////

from rest_framework import generics
from recicle.models import Recicle
from recicle.serializers import RecicleSerializer

from django.views import View

# Create your views here.

#inicio.html
def recicle (request):
   # return render(request,"pages/recicle.html", {"dates": "nombre"}),
   return render(request,"pages/recicle.html")

def disponibles (request):
   # return render(request,"pages/recicle.html", {"dates": "nombre"}),
   return render(request,"pages/mostrardisponibles.html")

def create(request):
    formulario = RecicleForm(request.POST or None, request.FILES or None) #identificar todos los elementos enviados atravez del formulario 
    #guardar datos del libro,recepcionar
    if formulario.is_valid():
        formulario.save()
        return redirect("crudrecicle")
    return render(request,"crudrecicle/create.html",{"form":formulario})

def form(request):
    return render(request,"crudrecicle/forms.html")

def crudrecicle(request):
    prendas = Recicle.objects.all()#consulta de todos los registros{libros} apartir de este objeto 
    return render(request,"crudrecicle/mostrar.html", {"prendas": prendas})

def editarpe(request, id):
    prenda = Recicle.objects.get(id=id) #recolectando info de libro
    formulario = RecicleForm(request.POST or None, request.FILES or None, instance=prenda) #recuperar datos de form
    if formulario.is_valid() and request.POST:
        formulario.save()
    return render(request,"crudrecicle/editarpe.html",{"form": formulario}) #{form.html y formulario{variable declarada aqui.}

def deletepe(request, id):
    prenda = Recicle.objects.get(id=id)
    prenda.delete()
    return redirect ("crudrecicle") #conservarnos en la pagina de libros luego de eliminar


class RecicleList(generics.ListCreateAPIView):
    queryset = Recicle.objects.all()
    serializer_class = RecicleSerializer
    
class RecicleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recicle
    serializer_class = RecicleSerializer