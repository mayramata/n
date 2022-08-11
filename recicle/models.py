from django.db import models

# Create your models here.
#aqui se hara un modelo para elegir que material deseas donar.

class Recicle(models.Model):
    #atributos y tipo e dato
    name_materials = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    stock=models.IntegerField()
    color = models.CharField(max_length=100) 
    typeclothings = models.CharField(max_length=100)
    ilustration= models.ImageField(upload_to="picture/",verbose_name="ilustration",null=True)
    
    
 #muestra una fila en el administrador con los librros agregados por el superuser
    def _str_(self):
        fila = "Name_materials:" +self.name_materials + " Category:" + self.category
        return fila
    #borra el libro por el administrador jnto con la imagen registrada en la caprpeta picture por el libro guardado
    def deletepe(self,using=None, keep_parents=False):
        self.ilustration.storage.delete(self.ilustration.name)
        super().delete()