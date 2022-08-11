import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
#////////////

from django.http import HttpResponse, JsonResponse
from .forms import BookForm #del formulario
from .models import Libro
from rest_framework import generics
from librerias.models import Libro
from librerias.serializers import LibroSerializer

from django.views import View

# Create your views here.

# Create your views here.

#declarar funcion que envia una solicitud con un texto
#def inicio(request):
    #return HttpResponse("<h1>Bienvenido a la libreria</h1>")
def inicio(request):
    return render(request,"pages/inicio.html")
def nosotros(request):
    return render(request,"pages/nosotros.html")

def tocreate(request):
    formulario = BookForm(request.POST or None, request.FILES or None) #identificar todos los elementos enviados atravez del formulario 
    #guardar datos del libro,recepcionar
    if formulario.is_valid():
        formulario.save()
        return redirect("books")
    return render(request,"books/tocreate.html",{"form":formulario})

def form(request):
    return render(request,"books/form.html")

def books(request):
    libros = Libro.objects.all()#consulta de todos los registros{libros} apartir de este objeto 
    return render(request,"books/index.html", {"libros": libros})

def editar(request, id):
    libro = Libro.objects.get(id=id) #recolectando info de libro
    formulario = BookForm(request.POST or None, request.FILES or None, instance=libro) #recuperar datos de form
    if formulario.is_valid() and request.POST:
        formulario.save()
    return render(request,"books/editar.html",{"form": formulario}) #{form.html y formulario{variable declarada aqui.}

def delete(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect ("books") #conservarnos en la pagina de libros luego de eliminar


class LibroList(generics.ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    
class LibroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libro
    serializer_class = LibroSerializer