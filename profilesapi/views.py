

# Create your views here.
#mostrando apiview
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from profilesapi import serializers, models, permissions 
#para serializers
from rest_framework import viewsets #para viewsets
from rest_framework.authentication import TokenAuthentication
#para ara de login
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class WelcomeToTheApiView(APIView):
    """apiview de prueba"""
    serializer_class = serializers.WelcomeSerializer
    
    
    def get(self, request, format=None):
        #retornar lista(o dicionario)de caracteristicas del apiview
        an_apiview = [
         "Usamos metodos HTTP (get,post,pacth,puth,delete)", 
         "se hace aqui la logica de app y se mapea manualmente los url", 
        ]
        
        return Response({"message":"Hello User","an_apiview":an_apiview}) 
    #funciones de viewapi
    def post(self, request):
        """crea ms con nombre del user"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name =  serializer.validated_data.get('name')
            message = f"welcome user {name} to rest framework"
            return Response({"message": message })
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            #definiendo funciones
    def put(self, request, pk=None): # pk hace que no ocupemos declarar un id para actualizar un objeto
        
        """actualizar metodo"""
        return Response({"method" : "PUT"})
                                 
    def patch(self, request, pk=None):
        """hacer una actalizacion parcial update en el objeto, ejemplo act segundo nombre"""
        return Response({"method" : "PATCH"})
            
    def delete(self, request, pk=None):
        """borrar objeto """
        return Response({"method" : "DELETE"})
            
class WelcomeToViewSet(viewsets.ViewSet):
    """test y api viewset list,destroy, sobre los objetos"""

    serializer_class = serializers.WelcomeSerializer
    
    def list (self, request):
        """retornar nensaje de saludo """
        
        a_viewset = [
         "Usa acciones list,create,retrive,update, parcial,update", 
         " mapea manualmente los url en router", 
        ]
        
        #"""nuestra vista"""
        return Response({"message" : "hola", "a_viewset" : a_viewset})
    
    def create (self, request):
        """crear nuevo mensaje de hola """
        
        serializer = self.serializer_class(data=request.data) #se decara parametro serializers
        
        if serializer.is_valid(): #hereda la variable serializers
            name = serializer.validated_data.get('name')
            message = f"Hola usuario {name} bienvenido a viewset en rest framework"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
          #  funciones de viewset    
    def retrieve (self, request , pk=None):
         """obiene un objeto y su id""" #los mensajes con """t"""" tienen que estar ala misma altura que el return o lo que le siga
         return Response({"http_method" : "GET"})
            
    def update (self, request , pk=None):
         """actualizar un objeto"""
         
         return Response({"http_method" : "PUT"})
                
    def  Partial_update (self, request , pk=None):
        """actualiza parcialmente el objeto ej:sobre el seg nombre"""
        
        return Response({"http_method" : "PATCH"})
            
    def destroy (self, request , pk=None):
        """destruye un objeto"""
        
        return Response({"http_method" : "DELETE"})
            
class UserProfileViewSet(viewsets.ModelViewSet):
    # crear y actualizar perfiles
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name","email")
    
class UserLoginApiView(ObtainAuthToken):
 renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
  #agrega clases de render a el update o token que se abilitan por djangoadmin
 
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """maneja el crear, leer y actualizar elprofilefeed"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.UserProfileSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = ( permissions.UpdateOwnProfile,
        IsAuthenticatedOrReadOnly)
    
    def permorm_created(self, serializer):
        """setear el perfil de usuarui para el usuario que este logeado en la app"""
        serializer.save(user_profile=self.request.user)
 
        