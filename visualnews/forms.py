from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Noticia
from .models import Comentario
from .models import Puntuacion

class RegistroForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email'
        ]
        labels={
            'username':'Nombre de usuario',
            'first_name':'Nombre',
            'last_name':'Appellido',
            'email':'Correo'
        }
class NoticiaForm(forms.ModelForm):
    class Meta:
        model=Noticia
        fields=('titulo','texto','etiquetas')

class ComentarioForm(forms.ModelForm):
    class Meta:
        model=Comentario
        fields=('texto',)
        labels={'texto':''}
class PuntuacionForm(forms.ModelForm):
    class Meta:
        model=Puntuacion
        fields=('voto',)
        labels={'Voto':'Punto',}