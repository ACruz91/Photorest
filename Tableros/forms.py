from django.contrib.auth.models import User
from django.forms import ModelForm
from Usuarios.models import Perfil
from django.db import models
from django import forms
from .models import *

#--------------------------------------
#FORMS
#--------------------------------------


########################################################################
# Nombre: Formulario_Nuevo_Tablero
# Atributos: forms.ModelForm
# Descripcion:Consiste en un Formulario para la creacion de un Tablero
########################################################################
class Formulario_Nuevo_Tablero(forms.ModelForm):
	class Meta:
		model = Tablero