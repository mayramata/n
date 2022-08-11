from requests import request
from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
 """permite editar al usuario editar su perfil"""
 
 def has_object_permission(self, request, view, obj):
     if request.method in permissions.SAFE_METHODS:
         return True
     
     return obj.id == request.user.id
        
 class UpdateOwnStatus(permissions.BasePermission):
     """permite la actaluzacion del status feed del perfil"""        
     def has_object_permission(self, request, view, obj):
       """checa si el usuario intenta editar su perfil"""
       if request.method in permissions.SAFE_METHODS:
         return True
     
       return obj.user_profile == request.user.id