from django.shortcuts import get_object_or_404, render

# Create your views here.


from catalogo_libros.models import Libros


def listaLibros(request):
    libros = Libros.objects.all()
    return render(request, 'catalogo/lista_libros.html',
        {'libros':libros})


def detale_libro(request,id):
    libro = get_object_or_404(Libros,id=id)
    return render(request, 'catalogo/detalle_libros.html',
                {'libro':libro})