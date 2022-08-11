from rest_framework import serializers
#crear perfil de usuario  
from profilesapi import models

class WelcomeSerializer(serializers.Serializer):
    """campo para probar nuestro apiview"""
    name = serializers.CharField(max_length=10)
    

class UserProfileSerializer(serializers.ModelSerializer):
    """serializer objeto de perfil de usuario"""
    class Meta:
        model = models.UserProfile
        fields = ("id",  "email", "name","password") #deseamos mostrar
        extra_kwargs = {
            "password":{
                "write_only": True,
                "style": {"input_type" : "password"}
                
                }
            }
            
    def create(self, validated_data):
        """crear y retornar un nuevo usuario"""
        user = models.UserProfile.objects.create_user(
            email = validated_data["email"],
            name = validated_data["name"],
            password = validated_data["password"]
         
     )
        return user
     
    def update(self, instance, validated_data):
     #actualuza cuenta de usuario
     if "password" in validated_data:
        password = validated_data.pop("password")
        instance.set_password(password)
        
        return super().update(instance, validated_data)
        
class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """serializador de profile feed items"""    
     
    class Meta:
        model = models.ProfileFeedItem
        fields = ("id", "user_profile, status_text, create_on")  
        extra_kwargs = {"user_profile": {"read_only": True}}          