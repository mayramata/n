#formularios parametros
from django.contrib.auth.forms import UserCreationForm
from django import forms

#parametro del modelo
from profilesapi.models import UserProfile


"""   
from django.contrib.auth.models import User
class UserRegisterForm(UserCreationForm):
   email = forms.EmailField()

   class Meta:
       model = User
       fields = ['name', 'email', "password"]
    
"""       
    
class UserRegisterForm(UserCreationForm):

    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )

    class Meta:

        model = UserProfile
        fields = (
            'email',
            'name',
        )
        widgets = { 
                   'name': forms.TextInput(
                attrs={
                    'placeholder': 'nombres ...',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo Electronico ...',
                }
            ),
           
        }
    
    def clean_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['password']:
            self.add_error('password', 'Las contraseñas no son iguales')


