from django.urls import path
from catalogo_libros import views

urlpatterns = [
    path('',views.listaLibros,name='listaLibros'),
    path('libros/<int:id>',views.detale_libro,name='detalle_libro'),
]