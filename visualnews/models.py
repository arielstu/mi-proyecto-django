from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Noticia(models.Model):
    autor=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    titulo=models.CharField(max_length=200)
    texto=models.TextField()
    publico=models.BooleanField(default=False)
    fecha_creacion=models.DateTimeField(default=timezone.now)
    fecha_publicacion=models.DateTimeField(blank=True,null=True)
    etiquetas=models.CharField(max_length=255)
    puntos=models.IntegerField(default=0)

    def puntuar(self,punto):
        self.puntos+=punto
        self.save()

    def publicar(self):
        if self.fecha_publicacion==None:
            self.fecha_publicacion=timezone.now()
        self.publico=True
        self.save()

    def ocultar(self):
        self.publico=False
        self.save()

    
    def __str__(self):
        return self.titulo

class Puntuacion(models.Model):
    autor=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    noticia=models.ForeignKey('Noticia',on_delete=models.CASCADE)
    fecha_actualizacion=models.DateTimeField(default=timezone.now)
    voto=models.BooleanField(default=False)

    def __str__(self):
        return str(self.voto)

    def puntuar(self,voto):
        self.fecha_actualizacion=timezone.now()
        if voto==True:
            self.voto=voto
        else:
            self.voto=voto
        self.save()


class Comentario(models.Model):
    autor=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    noticia=models.ForeignKey('Noticia',on_delete=models.CASCADE)
    texto=models.TextField()
    fecha_publicacion=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.texto



