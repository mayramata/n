import email
from turtle import home
from django.db import models

# Create your models here.
class Employee(models.Model):
    name_empleado = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.IntegerField()
    date_register = models.DateTimeField()
    home= models.TextField()
    
class Costureras(models.Model):
    name_costurera =models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.IntegerField()
    date_register = models.DateTimeField()
    home= models.TextField()
    
