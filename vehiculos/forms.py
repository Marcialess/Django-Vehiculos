from django import forms
from .models import Vehiculo

class AddVehiculo(forms.ModelForm):
    class Meta:
        model = Vehiculo
        exclude = ['fecha_modificacion', 'fecha_creacion']