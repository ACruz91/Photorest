from django.utils.encoding import smart_unicode
from Categorias.models import Categoria
from Usuarios.models import Perfil
from django.db import models
from datetime import date
from Tableros.models import Tablero

#--------------------------------------
#MODELS
#--------------------------------------

#class Post
class Post(models.Model):
	titulo = models.CharField(max_length = 50, unique = True)
	imagen = models.ImageField(upload_to = 'post', blank = True)
	descripcion = models.TextField(max_length = 100, blank = True)
	fecha = models.DateTimeField(auto_now_add = True)
	creador = models.ForeignKey(Perfil, related_name = 'FK_USUARIO')
	categoria = models.ForeignKey(Categoria, related_name = 'FK_CATEGORIA')
	tablero = models.ForeignKey(Tablero, related_name = 'FK_TABLERO')
	def __unicode__(self):
		return self.titulo

#class Commentario
class Commentario(models.Model):
	id_usuario = models.ForeignKey(Perfil, related_name = 'FK_USUARIO_COMENTARIO')
	descripcion = models.TextField(max_length = 100)
	valor = models.IntegerField(default = 0)
	fecha = models.DateTimeField(auto_now_add = True)
	id_post = models.ForeignKey(Post, related_name = 'FK_POST_COMENTARIO')