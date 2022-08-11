from django.contrib import admin
from .models import Libro
# Register your models here.registra el modelo para cuando el administrador ya tenga la simulacion del objeto en este caso el libro del modelo de cla clase model.py

admin.site.register(Libro)