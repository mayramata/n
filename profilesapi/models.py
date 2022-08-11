from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# profiles add model item
from django.conf import settings

class UserProfileManager(BaseUserManager):
#manager para perfiles de usuarios
    def createnew_user(self, email, name, password=None):
        
#crear nuevo perfil del usuario

        if not email:  #coportamiento standar que espera django, pide un correo
            raise ValueError(" usuario debe de tener un email")
        #lovercase django cambie todo de mayusculas a minusculas 
        email = self.normalize_email(email)
        user = self.model(email=email, name=name) #define objeto
        
        #modelo definido, ahora el user ocupa un password y guardar en un hash
        user.set_password(password)
        user.save(using=self._db) #guardado en hash el usuario
        
        return user
    
    #definiendolo una funcion  para super usuario administrador
    def create_superuser(self, email,name, password):
        user = self.create_user(email, name, password)
        
        user.is_superuser = True #se esppecifica cuando tenemos permisos mexin
        user.is_staff = True
        user.save(using=self._db) #guardado en hash
        
        return user
                
class UserProfile(AbstractBaseUser, PermissionsMixin):
    #definirendo modelopara usuarios
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserProfileManager() #classe
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]
    
    
    # obtener nombre de usuario completo
    def get_full_name(self):
        return self.name
    # obtener nombre de usuario corto
    def get_short_name(self):
        return self.name #mostrar nombre
    
    #retorno de cadena del nombre de los usuarios
    def __str__(self):
        return self.email #mostrar email
    
class ProfileFeedItem(models.Model):
    """perfil de status update, actualizaciones"""
    
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    #si un ususario es borrado se borraran todos los post que este a hecho 
    #relacion one to one
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """retornar el modelo coomo cadena"""
        return self.status_text
    