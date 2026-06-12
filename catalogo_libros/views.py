from django.shortcuts import render

# Create your views here.


from catalogo_libros.models import Libros


def listaLibros(request):
    libros = Libros.objects.all()
    return render(request, 'catalogo/lista_libros.html',
        {'libros':libros})


