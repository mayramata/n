from dataclasses import field
from django import forms
from .models import Libro

class BookForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = "__all__" #todos los campos doble guion bajo
    