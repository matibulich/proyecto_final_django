from django.contrib import admin
from .models import Serie, Usuario, Pelicula


# Register your models here.
admin.site.register(Usuario)
admin.site.register(Pelicula)
admin.site.register(Serie)