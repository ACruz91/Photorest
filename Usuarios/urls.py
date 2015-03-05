from django.conf.urls import patterns, include, url
from Usuarios.views import *
from Usuarios import views
from .views import *


urlpatterns = patterns('',
	#URLs relacionadas con el Perfil
	url(r'^registro/$', views.Vista_Nuevo_Usuario, name='registro'),
	url(r'^nuevo_perfil/$', views.Vista_Nuevo_Perfil, name='rellenar_perfil'),
	url(r'^editar_perfil/$', views.Vista_Editar_Perfil, name='editar_perfil'),
	url(r'^perfil/$', views.Vista_Perfil, name='perfil'),
	url(r'^perfil/(?P<perfil_id>\d+)$', views.Vista_Perfil_Photorest, name='perfil_photorest'),
	url(r'^foto_perfil/(?P<perfil_id>\d+)$', views.Vista_Foto_Perfil, name='perfil_foto'),
	#URLs relacionadas con la Amistad
	url(r'^busqueda/$',Vista_Busquedad_Usuarios.as_view(), name='busqueda'),			
	url(r'^amigos/$', views.Vista_Lista_Amigos, name='amigos'),
	url(r'^amigos_amigo/(?P<id_perfil>\d+)$', views.Vista_Lista_Amigos_Perfil_Amigo, name='enviar'),
    url(r'^aviso/$', TemplateView.as_view(template_name='aviso_amistad.html'), name = 'avisar'),
    url(r'^peticiones/$', TemplateView.as_view(template_name='peticiones.html'), name = 'peticiones'),
	url(r'^enviar/(?P<id_perfil>\d+)$', views.Vista_Enviar_Peticion, name='enviar'),
	url(r'^aceptar/(?P<peticion_id>\d+)$', views.Vista_Aceptar_Peticion, name='enviar'),
	url(r'^rechazar/(?P<peticion_id>\d+)$', views.Vista_Rechazar_Peticion, name='enviar'),
	url(r'^enviadas/$', views.Vista_Ver_Peticion, name='enviadas'),
	url(r'^recibidas/$', views.Vista_Ver_Peticion_Recibida, name='recibidas'),
)