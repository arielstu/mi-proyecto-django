from django.contrib import admin

from .models import Noticia
from. models import Comentario

admin.site.register(Noticia)
admin.site.register(Comentario)

