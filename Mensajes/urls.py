from django.conf.urls import patterns, include, url
from Mensajes.views import *
from Mensajes import views
from .views import *


urlpatterns = patterns('',
	#Acciones
    url(r'^ver/$', TemplateView.as_view(template_name='ver_mensajes.html'), name = 'avisar'),
	url(r'^enviar/(?P<id_perfil>\d+)/$',views.Vista_Enviar_Mensaje, name='enviar'),
	url(r'^eliminar/(?P<id_mensaje>\d+)/$',views.Vista_Eliminar_Mensaje, name='eliminar'),
	#Listas
	url(r'^recibidos/$',views.Vista_Ver_Mensaje_Recibidos, name='ver'),	
	url(r'^enviados/$',views.Vista_Ver_Mensaje_Enviados, name='ver'),		
)