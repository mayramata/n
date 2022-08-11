from django.db import models


# Create your models here. aqui se agregaran los productos
class Product(models.Model):
    name_product = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    ilustration= models.ImageField(upload_to="picture/",verbose_name="ilustration",null=True)
    price=models.IntegerField()
    
    
    def __str__(self):
        return f"{self.name_product} -> {self.price}"
    
