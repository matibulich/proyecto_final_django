from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pelicula(models.Model):
    nombre= models.CharField(max_length=30)
    genero= models.CharField(max_length=30)
    plataforma= models.CharField(max_length=30)
    puntuacion=models.IntegerField()
    comentarios=models.CharField(max_length=300)

class Serie(models.Model):
    nombre= models.CharField(max_length=30)
    genero= models.CharField(max_length=30)
    plataforma= models.CharField(max_length=30)
    puntuacion=models.IntegerField()
    comentarios=models.CharField(max_length=300)

