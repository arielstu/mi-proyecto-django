from django.contrib import admin

from .models import Noticia
from. models import Comentario
from. models import Puntuacion

admin.site.register(Noticia)
admin.site.register(Comentario)
admin.site.register(Puntuacion)

