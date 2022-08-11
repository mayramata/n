#venia vacia
from django.urls import path , include # este ayuda a incluir este urls de esta app a el urls del proyecto
#from recicle import views # importar solo esta vista

from . import views #importar todas las vistas
##se hacen solicitudes
#from django.conf import settings
from django.contrib.staticfiles.urls import static #archivos estaticos de imagenes




urlpatterns = [
    path("",views.buyers, name="buyers"),
]
