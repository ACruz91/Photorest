from django.utils.encoding import smart_unicode
from Usuarios.models import Perfil
from django.db import models


########################################################################
# Nombre: Tablero
# Atributos: models.Model
# Descripcion:Consiste en un modelo para un Tablero en el que tiene que
# tener asociado un Post y agrega un conjunto de Post, el Tablero lo
# puede crear el usuario
########################################################################
class Tablero(models.Model):
	nombre = models.CharField(max_length = 50, unique = True)
	imagen = models.ImageField(upload_to = 'categoria', verbose_name='Categoria')
	creador = models.ForeignKey(Perfil, related_name = 'FK_USUARIO_TABLERO')
	def __unicode__(self):
		return self.nombre