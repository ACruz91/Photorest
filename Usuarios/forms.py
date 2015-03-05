from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from datetime import datetime 
from django import forms
from .models import *


########################################################################
# Nombre: Formulario_Nuevo_Usuario
# Atributos: UserCreationForm
# Descripcion:Consiste en un Formulario para la creacion de un Usuario
########################################################################

class Formulario_Nuevo_Usuario(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username = username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Ya existe un usuario con este nombre.")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError("No coinciden las dos contrasenas.")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_staff = False
        user.is_superuser = False
        if commit:
            user.save()
        return user

########################################################################
# Nombre: Formulario_Usuario
# Atributos: UserCreationForm
# Descripcion:Consiste en un Formulario para editar el Usuario
########################################################################

class Formulario_Usuario(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')        

########################################################################
# Nombre: Formulario_Perfil
# Atributos: forms.ModelForm
# Descripcion:Consiste en un Formulario para la creacion del Usuario
# y para editar el Usuario
########################################################################

class Formulario_Perfil(forms.ModelForm):
    class Meta:
       model = Perfil
       exclude = ('usuario', 'puntos', 'amigos')

########################################################################
# Nombre: Formulario_Amistad_Peticion
# Atributos: forms.ModelForm
# Descripcion:Consiste en un Formulario para las peticiones de amistad
# entre un usuario y otro.
########################################################################

class Formulario_Amistad_Peticion(forms.ModelForm):
    class Meta:
        model = Amistad
        fields = ('mensaje_peticion',)

    def __init__(self, *args, **kwargs):
        super (Formulario_Amistad_Peticion, self).__init__(*args, **kwargs)
        self.fields ['mensaje_peticion'].label = "mensaje_peticion"

    def save (self, commit = True):
        peticion = super (Formulario_Amistad_Peticion, self).save (commit = False)
        if commit:
            peticion.fecha_peticion = datetime.now()
            peticion.save ()
        return peticion        