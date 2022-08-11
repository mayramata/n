from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Libro(models.Model):
    id:models.AutoField(primary_key=True)
    title = models.CharField(max_length=255,verbose_name="title")
    author = models.CharField(max_length=255,verbose_name="author")
    genres = models.CharField(max_length=255,verbose_name="genres")
    editorial = models.CharField(max_length=255)
    ilustration= models.ImageField(upload_to="picture/",verbose_name="ilustration",null=True)
    description=models.TextField(verbose_name="Description",null=True)
    
    #muestra una fila en el administrador con los librros agregados por el superuser
    def _str_(self):
        fila = "Title:" +self.title + " description:" + self.description
        return fila
    #borra el libro por el administrador jnto con la imagen registrada en la caprpeta picture por el libro guardado
    def delete(self,using=None, keep_parents=False):
        self.ilustration.storage.delete(self.ilustration.name)
        super().delete()