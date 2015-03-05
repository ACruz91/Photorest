from django.utils.encoding import smart_unicode
from django.db import models


########################################################################
# Nombre: Categoria
# Atributos: models.Model
# Descripcion: Modelo para una Categoria de Photorest, cada Post debe
# de tener una Categoria asociada
########################################################################

class Categoria(models.Model):
	nombre = models.CharField(max_length = 50, unique = True)
	descripcion = models.CharField(max_length = 100, blank = True)
	imagen = models.ImageField(upload_to = 'categoria', verbose_name='Categoria')

	def __unicode__(self):
		return self.nombre