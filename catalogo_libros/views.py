from django.contrib import messages
from django.shortcuts import get_object_or_404, render,redirect

# Create your views here.


from catalogo_libros.models import Libros
from catalogo_libros.forms import LibrosForm

def listaLibros(request):
    libros = Libros.objects.all()
    return render(request, 'catalogo/lista_libros.html',
        {'libros':libros})


def detale_libro(request,id):
    libro = get_object_or_404(Libros,id=id)
    return render(request, 'catalogo/detalle_libros.html',
                {'libro':libro})

def crearLibro(request):
    if request.method == 'POST':
        form = LibrosForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Libro creado correctamente')
            return redirect('crearLibro')
        else:
            print('llega al error ',form.errors)
            messages.error(request,'Error al crear libro')
    else:
        form = LibrosForm()

    return render(request,'catalogo/crear_libro.html',{ 'form':form })
