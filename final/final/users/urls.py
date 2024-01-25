from django.urls import path
from users.views import (
logIn, 
registro, 
index, 
leer_blogs, 
acerca_de_mi, 
escribir_blog, 
eliminar_post, 
edit_blog,
detalle,
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', logIn, name='login'),
    path('registro', registro, name='registro'),
    path('', index, name='index'),
    path('blogs', leer_blogs, name='blogs' ),
    path('acerca', acerca_de_mi, name='about'),
    path('posteo', escribir_blog, name='posteo'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('eliminar/<posteo>', eliminar_post, name='eliminarpost'),
    path('editpost/<posteo>', edit_blog, name='editar'),
    path('detalleblog/<posteo>', detalle, name='detalle'),
]
