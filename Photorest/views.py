from django.shortcuts import render_to_response,render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponse  
from Usuarios.models import *


########################################################################
# Nombre: Inicio
# Atributos: request
# Descripcion: Consiste en una vista para redireccionar a index.html
########################################################################

def inicio(request):
    return render(request,'index.html') 

########################################################################
# Nombre: user_login
# Atributos: request
# Descripcion: Consiste en un login para el usuario
########################################################################

def Login_Usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            userr = request.POST['username']
            passwd = request.POST['password']
            access = authenticate(username=userr, password=passwd)
            if access is not None:
                if access.is_active:
                    login(request, access)
                    return  HttpResponseRedirect('/Usuarios/nuevo_perfil')
                else:
                    return render(request, 'ini/inactive.html')         
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request,'login.html', context)

########################################################################
# Nombre: logout_view
# Atributos: request
# Descripcion: Consiste salirse del sistema y una vez salido del sistema
# redirecciona a la raiz de la pagina
########################################################################

def Logout_Usuario(request):
    logout(request)
    return  HttpResponseRedirect('/')
