from django.conf.urls import patterns,include, url
from .views import *

urlpatterns = patterns('',
	#Tablero
	url(r'^lista/$', Vista_Lista_Tableros.as_view(), name = 'list'),
	url(r'^lista_amigos/(?P<Perfil_id>\d+)$', Vista_Lista_Tableros_Amigos.as_view(), name = 'list'),	
	url(r'^lista/(?P<Tablero_id>\d+)$', Vista_Lista_Tablero_Post.as_view(), name='detail'),
	url(r'^nuevo/$', Vista_Nuevo_Tablero.as_view(), name='detail'),


)