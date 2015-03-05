from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic.base import View
from django.conf import settings
from .models import *
from .forms import *


#--------------------------------------
#VIEWS
#--------------------------------------

#View para Nuevo Post
class Nuevo_Post(View):
    form_class = Formulario_Nuevo_Post
    template_nombre = 'nuevo.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()        
        return render(request, self.template_nombre, {'form': form, 'user':request.user})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():    
            form.save()
            return redirect('/Post/posts_usuario/')
        return render(request, self.template_nombre, {'form': form,})

#View para Lista Post Global
class Lista_Post(View):
    template_nombre = 'home.html'
    def get(self, request, *args, **kwargs):
        list = Post.objects.all().order_by('-fecha')
        return render(request, self.template_nombre, {'list':list,})

#View para Lista de Post de Usuario
class Lista_Posts_Usuario(View):
    template_nombre = 'posts_perfil.html'
    def get(self, request, *args, **kwargs):
        list = Post.objects.filter(creador = request.user.id).order_by('-fecha')
        return render(request, self.template_nombre, {'list':list,})

#View para Lista de Post de Usuario Amigo
class Lista_Posts_Usuario_Amigo(View):
    template_nombre = 'posts_perfil_amigo.html'
    def get(self, request, *args, **kwargs):
        id = self.kwargs['Perfil_id']
        perfil = Perfil.objects.get(pk = id)
        list = Post.objects.filter(creador = id).order_by('-fecha')
        return render(request, self.template_nombre, {'list':list, 'perfil' : perfil})

#View para detalles del Post
class Detalles_Post(View):
    template_nombre = 'detalles.html'
    form_class = Formulario_Nuevo_Comentario

    def get(self, request, *arg, **kwargs):
        id = self.kwargs['Post_id']
        post = get_object_or_404(Post, pk = id)     
        form = self.form_class()
        commentario = Commentario.objects.filter(id_post = id)
        return render(request,self.template_nombre,{'post' : post, 'commentario':commentario,  'form': form, 'user':request.user})

#Addicionar Comentario para Post
    def post(self, request, *args, **kwargs):
        id = self.kwargs['Post_id']
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():    
            form.save()
            return redirect('/Post/lista/'+id)

        return render(request, self.template_nombre, {'form': form})

#Editar el Post
class Editar_Post(View):
    form_class = Formulario_Editar_Post
    template_name = 'editar_post.html'

    def dispatch(self, *args, **kwargs):
        return super(Editar_Post, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        id = self.kwargs['Post_id']
        post = get_object_or_404(Post, pk = id)
        form = self.form_class(instance = post)
        return render(request, self.template_name, {'form': form, 'post' : post})

    def post(self, request, *args, **kwargs):
        id = self.kwargs['Post_id']
        post = get_object_or_404(Post, pk = id)
        form = self.form_class(request.POST, request.FILES, instance = post)

        if form.is_valid():
             form.save()
             return redirect('/Post/lista/'+id)
        return render(request, self.template_name, {'form': form})

#View para Eliminar el Post
class Eliminar_Post(View): 
    def get(self, request, *args, **kwargs):
        id = self.kwargs['Post_id']
        post = get_object_or_404(Post, pk = id)    
        post.delete()
        return redirect('/Post/posts_usuario/')

#View para Eliminar el Comentario
class Eliminar_Commentario(View): 
    def get(self, request, *args, **kwargs):
        id = self.kwargs['Comentario_id']
        id2 = self.kwargs['Post_id']
        comentario = get_object_or_404(Commentario, pk = id)
        comentario.delete()
        return redirect('/Post/lista/'+id2)

