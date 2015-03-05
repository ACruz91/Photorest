from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from Photorest import views
from .views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #Index
    url(r'^$', TemplateView.as_view(template_name='index.html'), name = 'index'),

    #Login
    url(r'^login/$','Photorest.views.Login_Usuario', name = 'login'),
    url(r'^logout/$','Photorest.views.Logout_Usuario', name='out'),
    
    #Admin
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #Mis Aplicaciones
    url(r'^Usuarios/', include('Usuarios.urls',namespace="Usuarios")),
    url(r'^Post/', include('Post.urls',namespace="Post")),
    url(r'^Categorias/', include('Categorias.urls',namespace="Categoria")),
    url(r'^Mensajes/', include('Mensajes.urls',namespace="Mensajes")),
    url(r'^Tableros/', include('Tableros.urls',namespace="Tableros")),

)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
