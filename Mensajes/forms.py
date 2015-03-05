from django.contrib.auth.models import User
from django.forms import ModelForm
from datetime import datetime 
from django import forms
from .models import *

########################################################################
# Nombre: Formulario_Nuevo_Mensaje
# Atributos: forms.ModelForm
# Descripcion:Consiste en un Formulario para mandarle mensajes privados.
########################################################################

class Formulario_Nuevo_Mensaje(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ('mensaje_privado',)

    def __init__(self, *args, **kwargs):
        super (Formulario_Nuevo_Mensaje, self).__init__(*args, **kwargs)
        self.fields ['mensaje_privado'].label = "mensaje_privado"

    def save (self, commit = True):
        form = super (Formulario_Nuevo_Mensaje, self).save (commit = False)
        if commit:
            form.fecha_peticion = datetime.now()
            form.save ()
        return form     