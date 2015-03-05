from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.http import HttpResponse
from django.conf import settings
from Post.models import Post
from .models import *

#--------------------------------------
#VIEWS
#--------------------------------------

########################################################################
# Nombre: Vista_Lista_Categoria
# Atributos: View
# Descripcion:Consiste en una vista para mostrar una lista de Categorias
########################################################################
class Vista_Lista_Categoria(View):
	template_nombre = 'lista_categorias.html'

	def get(self, request, *args, **kwargs):
		list = Categoria.objects.all().order_by('nombre')
		return render(request, self.template_nombre, {'list':list,})


########################################################################
# Nombre: Vista_Lista_Categoria_Post
# Atributos: View
# Descripcion:Consiste en una vista para mostrar una lista de Post cuya
# Categoria tiene asociada
########################################################################
class Vista_Lista_Categoria_Post(View):
	template_nombre = 'categoria.html'

	def get(self, request, *arg, **kwargs):
		id = self.kwargs['Categoria_id']
		list = Post.objects.filter(categoria = id)
		titulo = Categoria.objects.get(id = id)
		return render(request,self.template_nombre,{'list' : list, 'titulo' : titulo})