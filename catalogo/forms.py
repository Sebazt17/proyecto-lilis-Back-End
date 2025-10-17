from django import forms
from .models import Categoria, Producto


class CategoriaForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese nombre de la categoría'
        })
    )

    class Meta:
        model = Categoria
        fields = ['nombre']



class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese nombre del producto'
        })
    )

    ingredientes = forms.CharField(widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Ingrese los ingredientes del producto'
        })
    )

    tiempo_produccion = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 2 horas'
        })
    )

    descripcion = forms.CharField(widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Ingrese descripción del producto'
        })
    )

    imagen = forms.CharField(required=False,widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre de archivo o URL de la imagen'
        })
    )

    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )


    

    class Meta:
        model = Producto
        fields = ['nombre', 'ingredientes', 'tiempo_produccion', 'descripcion', 'imagen', 'categoria']
