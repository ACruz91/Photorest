from django.conf.urls import patterns, include, url

from Post import views
from .views import *

urlpatterns = patterns('',
	# Post
	url(r'^nuevo/$', Nuevo_Post.as_view(), name='nuevo'),
	url(r'^home/$', Lista_Post.as_view(), name='home'),
	url(r'^posts_usuario/$', views.Lista_Posts_Usuario.as_view(), name='posts'),
	url(r'^post_usuario_amigo/(?P<Perfil_id>\d+)$', Lista_Posts_Usuario_Amigo.as_view(), name='detalles'),
	url(r'^lista/(?P<Post_id>\d+)$', Detalles_Post.as_view(), name='detalles'),
	url(r'^editar/(?P<Post_id>\d+)$', Editar_Post.as_view(), name='editar'),
	url(r'^eliminar/(?P<Post_id>\d+)$', Eliminar_Post.as_view(), name='eliminar'),
	# Comentario
	url(r'^commentario/eliminar/(?P<Comentario_id>\d+)/(?P<Post_id>\d+)$', Eliminar_Commentario.as_view(), name='eliminar'),

)