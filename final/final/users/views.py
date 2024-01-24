from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required

from users.forms import BlogsForm, RegistrationForm
from users.models import Blog

import datetime

def index(request):
    return render(request, 'index.html')

def logIn(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                return render(request, 'ini.html', {'mensaje':f"Bienvenido {username}"})

            else:

                return render(request, 'ini.html', {'mensaje': 'Credenciales no válidas'})

        else:

            return render(request, 'ini.html', {'mensaje': 'no existe'})


    form = AuthenticationForm()

    return render(request, 'login.html', {'form':form})

def registro(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            nuevo = User(username=username)
            nuevo.set_password(form.cleaned_data.get('password1'))
            nuevo.save()

            return render(request, 'ini.html', {'mensaje': f'se dio de alta el usuario {username}'})
        else:
            return render(request, 'ini.html', {'mensaje': 'algo no esta bien'})
    form = RegistrationForm()
    return render(request, 'registro.html', {'form':form})

@login_required
def escribir_blog(request):
    if request.method == 'POST':
        form = BlogsForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            titulo = datos.get('titulo')
            subtitulo = datos.get('subtitulo')
            contenido = datos.get('contenido')
            autor = request.user
            creado = datetime.datetime.now()
            blog = Blog(titulo=titulo, subtitulo=subtitulo, contenido=contenido, autor=autor, creado=creado)
            blog.save()
            return render(request, 'ini.html')
        else:
            return render(request, 'ini.html')
    else:
        form = BlogsForm()
    return render(request, 'posteo.html', {'form':form})

def leer_blogs(request):
    blogs = Blog.objects.all()
    contexto ={'blogs':blogs}
    return render(request, 'leer_blogs.html', contexto)

def acerca_de_mi(request):
    return render(request, 'about.html')

def edit_blog(request, posteo):
    blog_edit = Blog.objects.get(titulo=posteo)
    if request.method == 'POST':
        fomulario = BlogsForm(request.POST)
        if fomulario.is_valid():
            blogeditado = fomulario.cleaned_data
            titulo = blogeditado.get('titulo')
            subtitulo = blogeditado.get('subtitulo')
            contenido = blogeditado.get('contenido')
            blog2 = Blog(titulo=titulo, subtitulo=subtitulo, contenido=contenido)
            blog2.save()
            return render(request, 'leer_blogs.html')
        else:
            return render(request, 'ini.html', {'mensaje': "no fue editado"})
    form = BlogsForm(initial={'titulo':blog_edit.titulo, 'subtitulo':blog_edit.subtitulo, 'contenido':blog_edit.contenido})
    return render(request, 'editarpost.html', {'form': form})
    

def detalle(request):
    pass

def eliminar_post(request, posteo):

    blogpost = Blog.objects.get(titulo=posteo)
    blogpost.delete()
    blogs = Blog.objects.all()
    contexto = {'blogs': blogs}
    return render(request, 'leer_blogs.html', contexto)
