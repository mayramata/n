
from . import views
#venia vacia
from django.urls import path , include # este ayuda a incluir este urls de esta app a el urls del proyecto
#from recicle import views # importar solo esta vista

from . import views #importar todas las vistas
##se hacen solicitudes
#from django.conf import settings
from django.contrib.staticfiles.urls import static #archivos estaticos de imagenes
from django.contrib.auth import views as auth_view


urlpatterns = [
     path("",views.logins, name="menu"),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('loginuser/', auth_view.LoginView.as_view(template_name='pages/login.html'), name="loginuser"),
    path('logout/', auth_view.LogoutView.as_view(template_name='pages/logout.html'), name="logout"),
    #path('login/', auth_view.LoginView.as_view()),
    #path('logout/', auth_view.LogoutView.as_view()),
    
]
