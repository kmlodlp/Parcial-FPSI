from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    
    class Meta:
        model = Empleado
        fields = (
            'nom',
            'tipo',
            'dpto',
            'curso'
        )
        widgest = {
            'nom': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre Apellido',
                }
            )
        }
        
    def clean_nom(self):
        nombre = self.cleaned_data['nom']
        if len(nombre)<=3:
            raise forms.ValidationError("El nombre debe tener minimo 3 caracteres")
        return nombre