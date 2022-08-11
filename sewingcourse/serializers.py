from dataclasses import Field
from rest_framework import serializers
from sewingcourse.models import Course
from sewingcourse.models import Personalizedfabric
#from rest_framework.serializers import ModelSerializer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Course
        fileds = "__all__"
      
class PersonalizedfabricSerializer(serializers.ModelSerializer):
    class Meta:
        model= Personalizedfabric
        fileds = ["__all__"]
      