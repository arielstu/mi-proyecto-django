
from django.urls import path
from .views import RegistroUsuario
from django.contrib.auth.views import login
urlpatterns = [
    path('registro/',RegistroUsuario.as_view(),name="registrar"),
    path('login/',login,{'template_name':'visualnews/login.html'},name="login"),
    path('',RegistroUsuario.as_view(),name="index")
]