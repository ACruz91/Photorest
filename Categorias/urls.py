from django.conf.urls import patterns,include, url
from .views import *

urlpatterns = patterns('',
	#Categoria
	url(r'^lista/$', Vista_Lista_Categoria.as_view(), name = 'list'),
	url(r'^lista/(?P<Categoria_id>\d+)$', Vista_Lista_Categoria_Post.as_view(), name='detail'),

)