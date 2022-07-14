from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Carga_peliculas(forms.Form):

    plataforma_opc =(
        ("netf","Netflix"),
        ("amz","Amazon"), 
        ("hbo","HBO"), 
        ("dsny","Disney"),
        ("appl","Apple"), 
        ("cine","Cine"), 
         
    )


    nombre = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    plataforma = forms.ChoiceField(choices=plataforma_opc)
    puntuacion = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '1 al 10'}), max_value=10, min_value=1)
    comentarios= forms.CharField(widget=forms.Textarea)







class Carga_series(forms.Form):

    nombre = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    plataforma = forms.CharField(max_length=30)
    puntuacion = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '1 al 10'}), max_value=10, min_value=1)
    comentarios= forms.CharField(widget=forms.Textarea)


class Usuario_registro(UserCreationForm):
    
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Repite la contraseña', widget=forms.PasswordInput)
    email = forms.EmailField()
    last_name: forms.CharField()
    first_name: forms.CharField()

    class Meta:
        model = User                                               
        fields = ['username',  'password1', 'password2','email', 'last_name', 'first_name']
        labels = {'username': 'Usuario', 'email':'Correo','last_name': 'Apellido', 'first_name':'Nombre'}
        help_texts= {k:"" for k in fields}
