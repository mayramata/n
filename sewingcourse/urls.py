#venia vacia
from django.urls import path , include
from . import views
#from django.contrib import admin
from sewingcourse import views
##se hacen solicitudes
from django.conf import settings
from django.contrib.staticfiles.urls import static #archivos estaticos de imagenes




urlpatterns = [
    path("",views.sewingcourse, name="sewingcourse"),
    path("productlist/", views.listcourse, name="listCourse"),#del api_view en views.py
]
