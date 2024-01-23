from django.urls import path
from users.views import logIn, registro, index, leer_blogs, acerca_de_mi, escribir_blog
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', logIn, name='login'),
    path('registro', registro, name='registro'),
    path('', index, name='index'),
    path('blogs', leer_blogs, name='blogs' ),
    path('acerca', acerca_de_mi, name='about'),
    path('posteo', escribir_blog, name='posteo'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
]
