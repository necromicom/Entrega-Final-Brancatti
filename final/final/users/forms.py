from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class BlogsForm(forms.Form):

    titulo = forms.CharField(max_length=50)
    subtitulo = forms.CharField(max_length=30)
    contenido = forms.CharField(max_length=10000)
   

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=20)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "password1", "password2", 'email']



class UserEditForm(UserCreationForm):
    
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["password1", "password2"]