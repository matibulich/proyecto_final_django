from django.urls import path

from movie_app import views






urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('formulario_inicio', views.formulario_inicio, name='formulario_inicio'),
    path('registrado', views.yaregistrado, name='yaregistrado'),
    path('portal', views.portal, name='portal'),
    path('peliculas', views.peliculas, name='peliculas'),
    path('series', views.series, name='series'),  
   

    
]

