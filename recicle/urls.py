#venia vacia
from django.urls import path , include # este ayuda a incluir este urls de esta app a el urls del proyecto
#from recicle import views # importar solo esta vista

from . import views #importar todas las vistas
##se hacen solicitudes
#from django.conf import settings
from django.conf import settings
from django.contrib.staticfiles.urls import static #archivos estaticos de imagenes
from recicle.views import RecicleList, RecicleDetail #se declara para enviar desde esta aplicacion



urlpatterns = [
    
    #inicio y 
    path("",views.recicle, name="recicle"),
    #entrar en carpeta crudrecicle
    path("crudrecicle", views.crudrecicle, name="crudrecicle"),#mosrar documento html
    path("donacioneslist", views.disponibles, name="donacioneslist"),#mosrar documento html
    #crudrecicle funciones
    path("crudrecicle/create", views.create, name="create"),
    path("crudrecicle/editarpe", views.editarpe, name="editarpe"),
    path("crudrecicle/editarpe/<int:id>", views.editarpe, name="editarpe"),
    path("deletepe/<int:id>", views.deletepe, name="deletepe"), #pasar un id del libro antes de hacer el borrado
    
     path("crudrecicle/<int:pk>", RecicleDetail.as_view()),
    path("crudrecicle/", RecicleList.as_view()),
]
