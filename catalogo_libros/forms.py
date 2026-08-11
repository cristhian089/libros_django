from django import forms
from catalogo_libros.models import Libros

class LibrosForm(forms.ModelForm):

    class Meta:
        model = Libros
        fields = '__all__' #('nombre','apellido','genero','editora') llama todos los campos del formulario
