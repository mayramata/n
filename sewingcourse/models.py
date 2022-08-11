from django.db import models

# Create your models here.

from distutils.command.upload import upload #imagenes

# Create your models here.
#aqui se ara una estructura para agregar cursos de costura
class Course(models.Model):
    name_course = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    number_course = models.IntegerField()
    teacher = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    ilustration= models.ImageField(upload_to="picture/",verbose_name="ilustration",null=True)
    discount = models.IntegerField()
    price = models.DecimalField(decimal_places=2,max_digits=6)
    #buyer = models.ForeignKey(Buyer, null=True,blank=True, on_delete= models.CASCADE)
 
    def __str__(self):
        return self.name_course
    
class Personalizedfabric (models.Model):
    name_desing = models.CharField(max_length=100)
    type_fabric = models.CharField(max_length=100)
    price = models.IntegerField()
    fabric_roll = models.IntegerField()
    size_roll = models.IntegerField()
    characterictics = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    ilustration= models.ImageField(upload_to="picture/",verbose_name="ilustration",null=True)
    discount = models.IntegerField()
    price = models.DecimalField(decimal_places=2,max_digits=6)
    
    def __str__(self):
        return self.name_desing