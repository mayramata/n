#venia vacia
from django.urls import path , include
from . import views
from shoppingcart import views
from django.contrib import admin
#from django.contrib import admin
##se hacen solicitudes
from django.contrib.staticfiles.urls import static #archivos estaticos de imagenes
from django.conf import settings

#from shoppingcart.views import Shoppingcart, Addproduct, Deleteproduct, Subtractproduct, Cleancar

from shoppingcart.views import Shoppingcart,agregar_producto, eliminar_producto, restar_producto, limpiar_carrito
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.Shoppingcart, name="shoppingcart"), #tienen que ser de preferwecia iguales y ya el index.html puede tener otro nombre en el def
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:product_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
