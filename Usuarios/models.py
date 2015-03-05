from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User
from django.db import models
from datetime import date


elegir_sexo=(
	('Hombre','Hombre'),
	('Mujer','Mujer'),
)

########################################################################
# Nombre: Perfil
# Atributos: models.Model
# Descripcion:Consiste en un modelo para el Perfil de la pagina cada
# Usuario posee un Perfil que tiene un atributo "usuario" que lo asocio
# con la clase User para tener los atributos de la clase User
########################################################################

class Perfil(models.Model):
	usuario = models.ForeignKey(User, unique = True, related_name = 'perfil')
	imagen = models.ImageField(upload_to = 'Foto', blank = True, null = True, verbose_name = 'FotoPerfil', default = 'default.png')
	edad = models.IntegerField( blank = True, null = True)
	fecha_nacimiento = models.DateField( blank = True, null = True)
	sexo = models.CharField(max_length = 25, choices = elegir_sexo)
	pais = models.CharField(max_length = 25, blank = True, null = True)
	localidad = models.CharField(max_length = 25, blank= True, null = True)
	amigos = models.ManyToManyField('Perfil', default = 'None', blank = True, null = True, related_name = 'amistades')
	puntos = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.usuario.username

########################################################################
# Nombre: Amistad
# Atributos: models.Model
# Descripcion:Consiste en un modelo para crear la amistad entre dos 
# usuarios
########################################################################

class Amistad(models.Model):
	usuario_nombre_peticion = models.CharField(max_length = 25)
	usuario_nombre_recibo = models.CharField(max_length = 25)
	fecha_peticion = models.DateField(blank=True,null=True)
	mensaje_peticion = models.TextField(blank=True,null=True)
	usuario_id_peticion = models.IntegerField()
	usuario_id_recibo = models.IntegerField()
