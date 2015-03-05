from django.shortcuts import render, redirect,render_to_response, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView,FormView
from django.utils.decorators import method_decorator
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic.base import View
from django.conf import settings
from .forms import *
from Usuarios.models import *
from Mensajes.models import *

########################################################################
# Nombre: Vista_Enviar_Mensaje
# Atributos: request
# Descripcion:Consiste en una vista para enviar mensajes privados
########################################################################
def Vista_Enviar_Mensaje(request, id_perfil):
	mi_perfil = Perfil.objects.get(usuario = request.user)
	perfil = Perfil.objects.get(pk = id_perfil)
	if request.method == 'POST':
		mensaje = Mensaje.objects.create(usuario_nombre_peticion = mi_perfil.usuario.username, usuario_nombre_recibo = perfil.usuario.username, usuario_id_peticion = mi_perfil.id, usuario_id_recibo = perfil.id)
		form = Formulario_Nuevo_Mensaje(request.POST, instance = mensaje)
		if form.is_valid():
			form.save()
			return redirect('/Usuarios/perfil/')
		else:
			pass
	else:
		form = Formulario_Nuevo_Mensaje()
		context = {'form' : form, 'perfil' : perfil}
		return render (request, 'nuevo_mensaje.html', context)


########################################################################
# Nombre: Vista_Eliminar_Mensaje
# Atributos: request
# Descripcion:Consiste en una vista para eliminar mensajes privados
########################################################################

def Vista_Eliminar_Mensaje(request,id_mensaje):
    mensaje = Mensaje.objects.get(id = id_mensaje)
    mensaje.delete()
    return redirect ('/Mensajes/ver/')

########################################################################
# Nombre: Vista_Ver_Mensaje_Recibidos
# Atributos: request
# Descripcion:Consiste en una vista para ver los mensajes que te han
# enviado
########################################################################

def Vista_Ver_Mensaje_Recibidos(request):
	mi_perfil= Perfil.objects.get(usuario = request.user)	
	list = Mensaje.objects.filter(usuario_id_recibo = mi_perfil.id)
	context = {'list' : list}
	return render (request, 'ver_mensajes_recibidos.html', context)

########################################################################
# Nombre: Vista_Ver_Mensaje_Enviados
# Atributos: request
# Descripcion:Consiste en una vista para ver los mensajes que te has
# enviado
########################################################################

def Vista_Ver_Mensaje_Enviados(request):
    mi_perfil= Perfil.objects.get(usuario = request.user)
    list = Mensaje.objects.filter(usuario_id_peticion = mi_perfil.id)
    context = {'list' : list}
    return render (request, 'ver_mensajes_enviados.html', context)