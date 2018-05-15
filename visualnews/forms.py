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
            'email',
        ]
        labels={
            'username':'Nombre de usuario',
            'first_name':'Nombre',
            'last_name':'Appellido',
            'email':'Correo',
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Ingresa tu(s) nombre(s)'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Ingresa tu(s) apellido(s)'}),
            'email': forms.TextInput(attrs={'placeholder': 'Ingresa tu correo electronico'}),
        }
class NoticiaForm(forms.ModelForm):
    class Meta:
        model=Noticia
        fields=('titulo','texto','etiquetas')
        widgets = {
            'texto': forms.Textarea(attrs={'placeholder': 'Ingresa el texto.'}),
            'titulo': forms.TextInput(attrs={'placeholder': 'Ingresa el titulo.'}),
            'etiquetas': forms.TextInput(attrs={'placeholder': 'eje: etiqueta1, etiqueta2, etc.'}),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model=Comentario
        fields=('texto',)
        labels={'texto':''}
        widgets = {
            'texto': forms.Textarea(attrs={'placeholder': 'Deja tu comentario'}),
        }
class PuntuacionForm(forms.ModelForm):
    class Meta:
        model=Puntuacion
        fields=('voto',)
        labels={'Voto':'Punto',}