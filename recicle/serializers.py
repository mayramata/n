from dataclasses import Field
from rest_framework import serializers
from recicle.models import Recicle


class RecicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recicle
        fileds = ["__all__"]
      
