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
from .models import *

########################################################################
# Nombre: Vista_Nuevo_Usuario
# Atributos: request
# Descripcion:Consiste en una vista para la creacion de un nuevo Usuario
# a traves de un formulario
########################################################################

def Vista_Nuevo_Usuario(request):
    if request.method == 'POST':
        form = Formulario_Nuevo_Usuario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form =Formulario_Nuevo_Usuario()
    context = {'form':form}
    return render(request, 'registro.html',  context)

########################################################################
# Nombre: Vista_Perfil
# Atributos: request
# Descripcion:Consiste en una vista para la visualizacion del Perfil de
# la pagina
########################################################################

def Vista_Perfil(request):
	usuarios = User.objects.get(username = request.user)
	perfil = Perfil.objects.get(usuario = request.user)
	context = {'usuarios' : usuarios, 'perfil' : perfil}
	return render_to_response('perfil.html', context, context_instance = RequestContext(request))

########################################################################
# Nombre: Vista_Perfil_Photorest
# Atributos: request
# Descripcion:Consiste en una vista para la visualizacion del Perfil de
# otra persona
########################################################################

def Vista_Perfil_Photorest(request, perfil_id):
    usuarios = User.objects.get(pk = perfil_id)
    perfil = Perfil.objects.get(pk = perfil_id)
    context = {'usuarios' : usuarios, 'perfil' : perfil}
    return render_to_response('perfil_photorest.html', context, context_instance = RequestContext(request))

########################################################################
# Nombre: Vista_Lista_Amigos
# Atributos: request
# Descripcion:Consiste en una vista para la lista de tus amigos
########################################################################

def Vista_Lista_Amigos(request):
    perfil = Perfil.objects.get(usuario = request.user)
    amigos = perfil.amigos.all()
    context = {'perfil': perfil ,'amigos' : amigos}
    return render (request, 'lista_amigos.html', context)

########################################################################
# Nombre: Vista_Lista_Amigos_Perfil_Amigo
# Atributos: request
# Descripcion:Consiste en una vista para la visualizacion de la lista de
# los amigos de un amigo
########################################################################

def Vista_Lista_Amigos_Perfil_Amigo(request, id_perfil):
    perfil = Perfil.objects.get(pk = id_perfil)
    amigos = perfil.amigos.all()
    context = {'perfil': perfil ,'amigos' : amigos}
    return render (request, 'lista_amigos_perfil_amigo.html', context)

########################################################################
# Nombre: Vista_Busquedad_Usuarios
# Atributos: request
# Descripcion:Consiste en una vista para la busqueda de Usuarios, solo
# de Usuarios.
########################################################################

class Vista_Busquedad_Usuarios(TemplateView):
    def get(self,request,*args,**kwargs):
        error = False
        if 'usuario_buscado' in request.GET:
            usuario = request.GET['usuario_buscado']
            if not usuario:
                context = {'error' : error}
                return render_to_response ('busquedad_usuario.html', context, context_instance = RequestContext(request))
            else:
                busqueda = User.objects.get(username = usuario)
                usuario_filtrado = Perfil.objects.filter(id = busqueda.id)
                context = {'usuario_filtrado' : usuario_filtrado}
                return render_to_response ('resultado_busqueda.html', context, context_instance = RequestContext(request))
        else:
                context = {'error' : error}
                return render_to_response ('busquedad_usuario.html', context, context_instance = RequestContext(request)) 



########################################################################
# Nombre: Vista_Nuevo_Perfil
# Atributos: request
# Descripcion:Consiste en una vista para la creacion de un Perfil a
# partir de un Usuario
########################################################################

def Vista_Nuevo_Perfil(request):
	perfiles = Perfil.objects.filter(usuario = request.user)
	if perfiles.exists():
		return HttpResponseRedirect('/Usuarios/perfil/')

	else:
		if request.method == "POST":
			perfil_usuario = Perfil.objects.create(usuario = request.user)
			form = Formulario_Perfil(request.POST, request.FILES, instance = perfil_usuario)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/Usuarios/perfil/')
		else:
			form = Formulario_Perfil()
		context = {"form" : form}
		return render_to_response('nuevo_perfil.html', context, context_instance = RequestContext(request)) 

########################################################################
# Nombre: Vista_Editar_Perfil
# Atributos: request
# Descripcion:Consiste en una vista para editar el perfil creado
########################################################################

def Vista_Editar_Perfil(request):
    usuarios = get_object_or_404(User, username = request.user)
    perfiles = get_object_or_404(Perfil, usuario = request.user)
    if request.method == 'POST':
        form = Formulario_Usuario(request.POST, instance = usuarios)
        form2 = Formulario_Perfil(request.POST, request.FILES, instance = perfiles)

        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect('/Usuarios/perfil/')
    else:

        form = Formulario_Usuario(instance = usuarios)
        form2 = Formulario_Perfil(instance = perfiles)
        context = { 'form': form,  'form2': form2 }
    return render_to_response('editar_perfil.html', context, context_instance=RequestContext(request))	

########################################################################
# Nombre: Vista_Enviar_Peticion
# Atributos: request
# Descripcion:Consiste en una vista para enviar peticiones
########################################################################

def Vista_Enviar_Peticion(request,id_perfil):
    #Variable para la funcion
    encontrado = None
    amistad = []

    #Cuerpo de la Funcion
    mi_perfil = Perfil.objects.get(usuario = request.user)
    amistad = mi_perfil.amigos.all()
    perfil = Perfil.objects.get(pk = id_perfil)

    #Compruebo que exista la peticion
    if perfil.id in (x.id for x in amistad):
        encontrado = 1
    #Si existe llega la busquedad al perfil amigo
    if encontrado == 1:
        return redirect('/Usuarios/aviso/')
    #Si no existe creamos la peticion
    else:   
        if request.method == "POST":
            #Creo todos los campos manualmente menos el mensaje que se hace mediante el Formulario
            peticion_amigo = Amistad.objects.create(usuario_nombre_peticion = mi_perfil.usuario.username, usuario_nombre_recibo = perfil.usuario.username,usuario_id_peticion = mi_perfil.id, usuario_id_recibo = perfil.id)
            form = Formulario_Amistad_Peticion(request.POST, instance = peticion_amigo)
            if form.is_valid():
                form.save()
                return redirect('/Usuarios/enviar/'+id_perfil)
        else:
                peticion = Amistad.objects.filter(usuario_id_peticion = mi_perfil.id, usuario_id_recibo = perfil.id)
                if peticion.exists():
                    context = {'perfil' : perfil}
                    return render (request, 'peticion_enviada.html', context)
                else:
                    form = Formulario_Amistad_Peticion()
                    context = {'form' : form, 'perfil' : perfil}
                    return render (request, 'nueva_peticion.html', context)

########################################################################
# Nombre: Vista_Ver_Peticion
# Atributos: request
# Descripcion:Consiste en una vista ver las peticiones enviadas
########################################################################

def Vista_Ver_Peticion(request):
    mi_perfil= Perfil.objects.get(usuario = request.user)
    peticion = Amistad.objects.filter(usuario_id_peticion = mi_perfil.id)
    context = {'peticion' : peticion}
    return render (request, 'ver_peticion.html', context)

########################################################################
# Nombre: Vista_Ver_Peticion_Recibida
# Atributos: request
# Descripcion:Consiste en una vista ver las peticiones recibidas
########################################################################

def Vista_Ver_Peticion_Recibida(request):
    mi_perfil= Perfil.objects.get(usuario = request.user)
    peticion = Amistad.objects.filter(usuario_id_recibo = mi_perfil.id)
    context = {'peticion' : peticion}
    return render (request, 'ver_peticion_recibida.html', context)

########################################################################
# Nombre: Vista_Aceptar_Peticion
# Atributos: request, peticion_id
# Descripcion:Consiste en una vista para aceptar las peticiones
########################################################################

def Vista_Aceptar_Peticion(request, peticion_id):
    peticion = Amistad.objects.get(pk = peticion_id)
    usuario_peticion = Perfil.objects.get(id = peticion.usuario_id_peticion)
    usuario_recibo = Perfil.objects.get(id = peticion.usuario_id_recibo)
    usuario_peticion.amigos.add(usuario_recibo)
    usuario_recibo.amigos.add(usuario_peticion) 
    peticion.delete ()     
    context = {'usuario_peticion': usuario_peticion}
    return render (request, 'aceptar_peticion.html', context)

########################################################################
# Nombre: Vista_Rechazar_Peticion
# Atributos: request, peticion_id
# Descripcion:Consiste en una vista para rechazar peticiones
########################################################################

def Vista_Rechazar_Peticion(request, peticion_id):
    peticion = Amistad.objects.get (pk = peticion_id)
    peticion.delete ()
    context = {'peticion':peticion}
    return render (request, 'rechazar_peticion.html', context)

########################################################################
# Nombre: Vista_Foto_Perfil
# Atributos: request, perfil_id
# Descripcion:Consiste en una vista para ver la foto perfil mas grande
########################################################################

def Vista_Foto_Perfil(request, perfil_id):
    Foto = Perfil.objects.get(pk = perfil_id)
    context = {'Foto' : Foto}
    return render (request, 'foto_perfil.html', context)


