from ast import ListComp
from asyncio import mixins
from multiprocessing import context
from django.shortcuts import render
#def
from django.db.models import query
from django.shortcuts import render
from .serializers import CourseSerializer
from .serializers import PersonalizedfabricSerializer
from . import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.
#from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .models import Course
from .models import Personalizedfabric
from sewingcourse.serializers import CourseSerializer
from sewingcourse.serializers import PersonalizedfabricSerializer

# Create your views here.
def sewingcourse(request): #tiene que ir el nombre de la a´ñicacion aqui para pasarla como variable en url por medio de view.sewingcourse
    return render(request, 'pages/sewingcourse.html')

class CourseList (generics.ListCreateAPIView):
    serializer_class = Course.objects.all()
    queryset = Course.objects.all()
    
class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course
    serializer_class = CourseSerializer

@api_view(["GET", "POST"])
@permission_classes({IsAuthenticated}) #restinge a los usuarios que usen admin la vista de las caracteristicas del objeto del modelo por medio de fileds en el serializer.py

def listcourse(request):
    query = Course.objects.all()
    serializer_class = CourseSerializer(query, many=True)
    context={
        "serializer_class_data": serializer_class.data
    }
    return Response(serializer_class.data)

class PersonalizedfabricList (generics.ListCreateAPIView):
    serializer_class = Course.objects.all()
    queryset = Course.objects.all()

class PersonalizedfabricDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Personalizedfabric
    serializer_class = PersonalizedfabricSerializer    

 