from django.db import models

########################################################################
# Nombre: Mensaje
# Atributos: models.Model
# Descripcion:Consiste en un modelo para un Mensaje privado entre usuarios
########################################################################

class Mensaje(models.Model):
	usuario_nombre_peticion = models.CharField(max_length = 25)
	usuario_nombre_recibo = models.CharField(max_length = 25)
	fecha_peticion = models.DateField(blank=True,null=True)
	mensaje_privado = models.TextField(blank=True,null=True)
	usuario_id_peticion = models.IntegerField()
	usuario_id_recibo = models.IntegerField()



