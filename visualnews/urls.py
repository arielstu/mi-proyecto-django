
from django.urls import path
from .views import RegistroUsuario
from .views import inicio
from .views import noticia_nueva
from .views import noticia_editar
from .views import noticia
from .views import noticias
from .views import publicar
from .views import ocultar
from .views import eliminar
from .views import buscar
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
urlpatterns = [
    path('registro/',RegistroUsuario.as_view(),name="registrar"),
    path('login/',login,{'template_name':'visualnews/login.html'},name="login"),
    path('logout/',logout,{'template_name':'visualnews/index.html'},name="logout"),
    path('',inicio,name="index"),
    path('noticias/nueva/',noticia_nueva,name="noticia_nueva"),
    path('noticias/editar/<int:id>',noticia_editar,name="noticia_editar"),
    path('noticias/<int:id>/',noticia,name="noticia"),
    path('noticias/',noticias,name="noticias"),
    path('noticias/publicar/<int:id>/',publicar,name="publicar"),
    path('noticias/ocultar/<int:id>/',ocultar,name="ocultar"),
    path('noticias/eliminar/<int:id>/',eliminar,name="eliminar"),
    path('noticias/buscar/<str:clave>/',buscar,name="buscar"),
]