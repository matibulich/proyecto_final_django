from django.db import models

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

class Usuario(models.Model):
    nombre= models.CharField(max_length=30)
    email= models.EmailField(max_length=30)
    password= models.CharField(max_length=10)



