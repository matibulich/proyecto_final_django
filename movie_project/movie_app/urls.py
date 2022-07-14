from django.urls import path

from movie_app import views






urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('portal', views.portal, name='portal'),
    path('peliculas', views.peliculas, name='peliculas'),
    path('series', views.series, name='series'),
    path('login', views.login_request, name='login'),
    path('registro', views.registro, name='registro'), 
   

    
]

