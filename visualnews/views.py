from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistroForm
from  django.shortcuts import render
from .models import Noticia
from .models import Comentario
from .models import Puntuacion
from django.utils import timezone
from .forms import NoticiaForm
from .forms import ComentarioForm
from .forms import PuntuacionForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404      

class RegistroUsuario(CreateView):
    model=User
    template_name="visualnews/registrar.html"
    form_class=RegistroForm
    
    success_url=reverse_lazy('index')

def inicio(request):
    noticias=Noticia.objects.filter(publico=True).order_by('fecha_publicacion')
    usuario=str(request.user)
    return render(request,'visualnews/index.html',{'noticias':noticias,'usuario':usuario})

def noticia_nueva(request):
    if str(request.user)=='AnonymousUser':
        return redirect('login')
    if request.method=="POST":
        form=NoticiaForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.autor=request.user
            post.save()
            return redirect('noticias')
    else:
        usuario=str(request.user)
        form = NoticiaForm()
    return render(request,'visualnews/noticia_nueva.html',{'form':form,'usuario':usuario})

def noticia_editar(request,id):
    if str(request.user)=='AnonymousUser':
        return redirect('login')
    noticia = get_object_or_404(Noticia, id=id)
    if request.method=="POST":
        form=NoticiaForm(request.POST,instance=noticia)
        if form.is_valid():
            post=form.save(commit=False)
            post.autor=request.user
            post.save()
            return redirect('index')
    else:
        form = NoticiaForm(instance=noticia)
    usuario=str(request.user)
    return render(request,'visualnews/noticia_nueva.html',{'form':form,'usuario':usuario})

def noticia(request,id):
    usuario=str(request.user)
    noticia=Noticia.objects.get(id=id)
    if noticia.publico==False:
        return redirect('index')
    if request.method=="POST":
        try:
            form=ComentarioForm(request.POST)
            if form.is_valid() and str(request.user)!='AnonymousUser':
                comentario=form.save(commit=False)
                comentario.autor=request.user
                comentario.noticia=noticia
                comentario.save()
                return redirect('noticia',noticia.id)
        except:
            pass
        try:
            puntuacion1=Puntuacion.objects.get(noticia=noticia,autor=request.user)
            puntuacion2=Puntuacion.objects.get(noticia=noticia,autor=request.user)
            formp=PuntuacionForm(request.POST,instance=puntuacion1)
            if formp.is_valid() and str(request.user)!='AnonymousUser':
                    puntuacion1=formp.save(commit=False)
                    puntuacion1.autor=request.user
                    puntuacion1.noticia=noticia
                    puntuacion1.save()
                    if puntuacion1.voto and puntuacion1.voto != puntuacion2.voto :
                        noticia.puntuar(1)
                    elif puntuacion1.voto == False and puntuacion1.voto != puntuacion2.voto:
                        noticia.puntuar(-1)
                    return redirect('noticia',noticia.id)
        except:
            try:
                formp=PuntuacionForm(request.POST)
                if formp.is_valid() and str(request.user)!='AnonymousUser':
                        puntuacion=formp.save(commit=False)
                        puntuacion.autor=request.user
                        puntuacion.noticia=noticia
                        puntuacion.save()
                        if puntuacion.voto:
                            noticia.puntuar(1)
                        return redirect('noticia',noticia.id)
            except:
                pass
    form=ComentarioForm()
    formp=False
    if str(request.user)!='AnonymousUser':
        try:
            puntuacion=Puntuacion.objects.get(noticia=noticia,autor=request.user)
            formp=PuntuacionForm(instance=puntuacion)
        except:
            formp=PuntuacionForm()
    comentarios=Comentario.objects.filter(noticia=noticia).order_by('-fecha_publicacion')
    return render(request,'visualnews/noticia.html',{'noticia':noticia,'usuario':usuario,'comentarios':comentarios,'form':form,'formp':formp})

    
def noticias(request):
    usuario=str(request.user)
    if usuario=='AnonymousUser':
        return redirect('login')
    
    noticias=Noticia.objects.filter(fecha_creacion__lte=timezone.now(),autor=request.user).order_by('-fecha_publicacion')
    return render(request,'visualnews/noticias.html',{'noticias':noticias,'usuario':usuario})

def publicar(request,id):
    usuario=str(request.user)
    if usuario=='AnonymousUser':
        return redirect('login')
    noticia=Noticia.objects.get(id=id)
    if noticia.autor != request.user:
        return redirect('index')
    noticia.publicar()
    return redirect('noticias')

def ocultar(request,id):
    usuario=str(request.user)
    if usuario=='AnonymousUser':
        return redirect('login')
    noticia=Noticia.objects.get(id=id)
    if noticia.autor != request.user:
        return redirect('index')
    noticia.ocultar()
    return redirect('noticias')

def eliminar(request,id):
    usuario=str(request.user)
    if usuario=='AnonymousUser':
        return redirect('login')
    noticia=Noticia.objects.get(id=id)
    if noticia.autor != request.user:
        return redirect('index')
    noticia.delete()
    return redirect('noticias')

 
    
