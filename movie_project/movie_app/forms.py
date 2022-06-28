from django import forms


class Carga_peliculas(forms.Form):

    nombre = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    plataforma = forms.CharField(max_length=30)
    puntuacion = forms.IntegerField()
    comentarios= forms.CharField(max_length=300)

class Carga_series(forms.Form):

    nombre = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    plataforma = forms.CharField(max_length=30)
    puntuacion = forms.IntegerField()
    comentarios= forms.CharField(max_length=300)



