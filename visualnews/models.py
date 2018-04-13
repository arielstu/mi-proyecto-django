from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Noticia(models.Model):
    autor=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    titulo=models.CharField(max_length=200)
    texto=models.TextField()
    publico=models.BooleanField(False)
    fecha_creacion=models.DateTimeField(timezone.now)
    fecha_publicacion=models.DateTimeField(blank=True,null=True)
    etiquetas=models.CharField(max_length=255)
    puntos=models.IntegerField(blank=True,null=True)

    def publicar(self):
        self.fecha_publicacion=timezone.now()
        self.publico=True
        self.save()

    def ocultars(self):
        self.publico=False
        self.save()

    def __str__(self):
        return self.titulo

class Puntuacion(models.Model):
    autor=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    noticia=models.ForeignKey('Noticia',on_delete=models.CASCADE)
    fecha_actualizacion=models.DateTimeField(timezone.now)
    voto=models.BooleanField()

    def __str__(self):
        return str(self.voto)

    def puntuar(self,voto):
        self.fecha_actualizacion=timezone.now()
        self.voto=voto
        self.save()


class Comentario(models.Model):
    autor=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    noticia=models.ForeignKey('Noticia',on_delete=models.CASCADE)
    texto=models.TextField()
    publico=models.BooleanField(False)
    fecha_creacion=models.DateTimeField(timezone.now)
    fecha_publicacion=models.DateTimeField(blank=True,null=True)
    

    def publicar(self):
        self.fecha_publicacion=timezone.now()
        self.publico=True
        self.save()

    def ocultar(self):
        self.publico=False
        self.save()

    def __str__(self):
        return self.texto



