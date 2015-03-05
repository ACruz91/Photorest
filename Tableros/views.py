from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.http import HttpResponse
from django.conf import settings
from Post.models import Post
from Usuarios.models import Perfil
from .forms import *

#--------------------------------------
#VIEWS
#--------------------------------------

########################################################################
# Nombre: Vista_Lista_Tableros
# Atributos: View
# Descripcion:Consiste en una vista para mostrar una lista de Tableros
########################################################################

class Vista_Lista_Tableros(View):
	template_nombre = 'lista_tableros.html'

	def get(self, request, *args, **kwargs):                 
		list = Tablero.objects.filter(creador = request.user.id).order_by('nombre')
		return render(request, self.template_nombre, {'list':list,})

########################################################################
# Nombre: Vista_Lista_Tableros_Amigos
# Atributos: View
# Descripcion:Consiste en una vista para mostrar una lista de Tableros
# de los amigos
########################################################################

class Vista_Lista_Tableros_Amigos(View):
    template_nombre = 'lista_tableros.html'

    def get(self, request, *args, **kwargs):
        id = self.kwargs['Perfil_id']
        perfil = Perfil.objects.get(pk = id)                     
        list = Tablero.objects.filter(creador = id).order_by('nombre')
        return render(request, self.template_nombre, {'list':list,  'perfil' : perfil})


########################################################################
# Nombre: Vista_Lista_Tablero_Post
# Atributos: View
# Descripcion:Consiste en una vista para mostrar una lista de Post dentro
# Del Tablero
########################################################################
class Vista_Lista_Tablero_Post(View):
	template_nombre = 'tablero.html'

	def get(self, request, *arg, **kwargs):
		id = self.kwargs['Tablero_id']
		list = Post.objects.filter(tablero = id)
		titulo = Tablero.objects.get(id = id)
		return render(request,self.template_nombre,{'list' : list, 'titulo' : titulo})

########################################################################
# Nombre: Vista_Nuevo_Tablero
# Atributos: View
# Descripcion:Consiste en una vista para crear un nuevo Tablero
########################################################################

class Vista_Nuevo_Tablero(View):
    form_class = Formulario_Nuevo_Tablero
    template_nombre = 'nuevo_tablero.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_nombre, {'form': form, 'user':request.user})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():    
            form.save()
            return redirect('/Tableros/lista/')
        return render(request, self.template_nombre, {'form': form})
