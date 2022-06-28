from django.shortcuts import render

from movie_app.models import Pelicula, Usuario, Serie
from movie_app.forms import Carga_peliculas, Carga_series




# Create your views here.

def inicio(request):
      return render(request, "movie_app/inicio.html")

def yaregistrado(request):
      return render(request, "movie_app/yaregistrado.html")


def portal(request):

      return render(request, "movie_app/portal.html")


def formulario_inicio(request):
      if request.method == 'POST':
            
            usuario= Usuario (request.POST['nombre'], request.POST['email'], request.POST['password'])
            usuario.save()
            return render(request, "movie_app/formulario_inicio.html")

      return render(request, "movie_app/formulario_inicio.html")

#FORMULARIO PELICULAS
def peliculas(request):

      if request.method == 'POST':

            miFormulario = Carga_peliculas(request.POST) 



            if miFormulario.is_valid:   

                  informacion = miFormulario.cleaned_data
                  

                  pelicula = Pelicula (nombre=informacion['nombre'], genero=informacion['genero'], plataforma=informacion['plataforma'], puntuacion=informacion['puntuacion'], comentarios=informacion['comentarios']) 

                  pelicula.save()

                  return render(request, "movie_app/peliculas.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= Carga_peliculas() #Formulario vacio para construir el html

      return render(request, "movie_app/peliculas.html", {"miFormulario":miFormulario})


 #FORMULARIO SERIES     

def series(request):

      if request.method == 'POST':

            miFormulario1 = Carga_series(request.POST) 

            
            if miFormulario1.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario1.cleaned_data

                  serie = Serie (nombre=informacion['nombre'], genero=informacion['genero'], plataforma=informacion['plataforma'], puntuacion=informacion['puntuacion'], comentarios=informacion['comentarios']) 

                  serie.save()

                  return render(request, "movie_app/series.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario1= Carga_series() #Formulario vacio para construir el html

      return render(request, "movie_app/series.html", {"miFormulario1":miFormulario1})
