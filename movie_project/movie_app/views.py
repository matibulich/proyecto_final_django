from django.shortcuts import render

from movie_app.models import Pelicula, Serie
from movie_app.forms import Carga_peliculas, Carga_series, Usuario_registro
from django.contrib.auth.forms import AuthenticationForm,  UserCreationForm
from django.contrib.auth import login, logout, authenticate


def inicio(request):
      return render(request, "movie_app/inicio.html")


def portal(request):

      return render(request, "movie_app/portal.html")



#FORMULARIO PELICULAS
def peliculas(request):

      if request.method == 'POST':

            miFormulario = Carga_peliculas(request.POST) 



            if miFormulario.is_valid():   

                  informacion = miFormulario.cleaned_data

                  pelicula = Pelicula (nombre=informacion['nombre'], genero=informacion['genero'], plataforma=informacion['plataforma'], puntuacion=informacion['puntuacion'], comentarios=informacion['comentarios']) 
                 
                  pelicula.save()

                  return render(request, "movie_app/portal.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= Carga_peliculas() #Formulario vacio para construir el html

      return render(request, "movie_app/peliculas.html", {"miFormulario":miFormulario})


 #FORMULARIO SERIES     

def series(request):

      if request.method == 'POST':

            miFormulario1 = Carga_series(request.POST) 

            
            if miFormulario1.is_valid():   #Si pasó la validación de Django

                  informacion = miFormulario1.cleaned_data

                  serie = Serie (nombre=informacion['nombre'], genero=informacion['genero'], plataforma=informacion['plataforma'], puntuacion=informacion['puntuacion'], comentarios=informacion['comentarios']) 

                  serie.save()

                  return render(request, "movie_app/portal.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario1= Carga_series() #Formulario vacio para construir el html

      return render(request, "movie_app/series.html", {"miFormulario1":miFormulario1})


 #FORMULARIO LOGIN
 

def login_request(request):
      if request.method == 'POST':
            form = AuthenticationForm(request, data = request.POST) 
            if form.is_valid():

                  usuario = form.cleaned_data.get('username')
                  password = form.cleaned_data.get('password')

                  

                  user = authenticate(username = usuario , password = password)

         

                  if user is not None:
                        login(request, user)

                        return render (request, "movie_app/portal.html", )
                  else:
                  
                        return render (request, "movie_app/inicio.html", {"mensaje":"Error en los datos"})
            else:
                        return render(request, "movie_app/inicio.html", {"mensaje":"Contraseña o Usuario incorrecto, Intente de nuevo"})
      
      form = AuthenticationForm()
      return render(request, "movie_app/login.html", {'form': form} )

 #FORMULARIO LOGIN
def registro(request):
      
      if request.method == "POST":

            form = Usuario_registro(request.POST)

            if form.is_valid():
                  username = form.cleaned_data['username']
                 
                  form.save()

                  return render(request, "movie_app/login.html", {"mensaje": "usuario creado"})

      else: 
            form = Usuario_registro()

      return render(request, "movie_app/registro.html", {"form": form})