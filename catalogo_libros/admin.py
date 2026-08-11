from django.contrib import admin
from .models import Autor,Editora,Libros,Generos
# Register your models here.
admin.site.register(Autor)
admin.site.register(Editora)
admin.site.register(Libros)
admin.site.register(Generos)