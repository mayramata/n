from dataclasses import field
from django import forms
from .models import Recicle

class RecicleForm(forms.ModelForm):
    class Meta:
        model = Recicle
        fields = "__all__" #todos los campos doble guion bajo
    