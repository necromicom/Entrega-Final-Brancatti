from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=30)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)
    from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=30)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        contenido_resumido = self.contenido[:50] + '...' if len(self.contenido) > 50 else self.contenido
        return (
            f"Titulo: {self.titulo}\n"
            f"Subtítulo: {self.subtitulo}\n"
            f"Contenido: {contenido_resumido}\n"
            f"Autor: {self.autor}\n"
            f"Fecha de Creación: {self.creado}"
        )
