from dataclasses import Field
from rest_framework import serializers
from librerias.models import Libro


class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fileds = ["__all__"]
      
