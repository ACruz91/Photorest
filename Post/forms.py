#encoding: utf-8
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
# Nombre: Formulario_Nuevo_Post
# Atributos: forms.ModelForm
# Descripcion:Consiste en un Formulario para la creacion de un Post
########################################################################
class Formulario_Nuevo_Post(forms.ModelForm):
	class Meta:
		model = Post
		
########################################################################
# Nombre: Formulario_Nuevo_Comentario
# Atributos: forms.ModelForm
# Descripcion:Consiste en un Formulario para la creacion de un Comentario
########################################################################
class Formulario_Nuevo_Comentario(ModelForm):
	class Meta:
		model = Commentario

########################################################################
# Nombre: Formulario_Eitar_Post
# Atributos: forms.ModelForm
# Descripcion:Consiste en un Formulario para la edicion de un Post
########################################################################
class Formulario_Editar_Post(ModelForm):
	class Meta:
		model = Post
       	exclude = ('creador')
