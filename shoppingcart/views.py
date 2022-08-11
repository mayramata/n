
# Create your views here.
#para crear un una direccion d eurl en el nav se ocupa configurar setting,url de l proyecto, de la aplicacion perteneciente el urls,view.
from django.shortcuts import render, HttpResponse, redirect

from shoppingcart.Carcrud import Carrito
from shoppingcart.models import Product


def Shoppingcart(request):
    productos = Product.objects.all()
    return render(request, "pages/shopping.html", {'productos':productos})


def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Product.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("shoppingcart")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Product.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("shoppingcart")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Product.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("shoppingcart")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("shoppingcart")