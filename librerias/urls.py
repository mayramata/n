#venia vacia
from django.urls import path,include
from . import views
##se hacen solicitudes
from django.conf import settings
from django.contrib.staticfiles.urls import static #archivos estaticos de imagenes
#/////////////////////////////////////////////
from librerias.views import LibroList, LibroDetail #se declara para enviar desde esta aplicacion
 #se declara para enviar desde otra aplicacion los serilalizer de company
from django.urls import path
#aqui el usuario puede acceder a la vista por el navegador
#direccion del navegador y se usan para dar direccion href



urlpatterns = [
    path("",views.inicio, name="inicio"),
    path("nosotros", views.nosotros, name="nosotros"),
    path("books", views.books, name="books"),#mosrar documento html
    path("books/tocreate", views.tocreate, name="tocreate"),
    path("books/editar", views.editar, name="editar"),
    path("books/editar/<int:id>", views.editar, name="editar"),
    path("delete/<int:id>", views.delete, name="delete"), #pasar un id del libro antes de hacer el borrado
    
    path("libreria/<int:pk>", LibroDetail.as_view()),
    path("libreria/", LibroList.as_view()),
     
#pictures y root datos
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
