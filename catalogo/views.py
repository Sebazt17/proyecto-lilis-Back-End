from django.shortcuts import render, get_object_or_404
from catalogo.models import Categoria, Producto


# 🏠 Landing
def landing(request):
    return render(request, 'catalogo/landing.html')


# 📚 Catálogo principal (lista de categorías)
def catalogo(request):
    categorias = Categoria.objects.all()
    return render(request, 'catalogo/catalogo.html', {
        "categorias": categorias
    })


# 🍬 Subcatálogo (productos dentro de una categoría)
def subcatalogo(request, categoria):
    categoria_obj = get_object_or_404(Categoria, nombre=categoria)
    productos = Producto.objects.filter(categoria=categoria_obj)
    return render(request, "catalogo/subcatalogo.html", {
        "categoria": categoria_obj,
        "productos": productos
    })


# 🔍 Detalle de producto individual
def detalle_producto(request, producto):
    producto_obj = get_object_or_404(Producto, nombre=producto)
    categoria = producto_obj.categoria
    return render(request, "catalogo/detalle.html", {
        "producto": producto_obj.nombre,
        "detalle": producto_obj,
        "categoria": categoria.nombre
    })


# 🏢 Página empresa
def empresa(request):
    data = {
        "historia": "Dulcería Lilis nació en 1995...",
        "mision": "Endulzar la vida de nuestros clientes con productos artesanales.",
        "vision": "Ser reconocidos como la dulcería líder en innovación y calidad en la región.",
        "valores": ["Calidad", "Tradición", "Innovación", "Compromiso"],
        "contacto": "contacto@dulcerialilis.cl",
        "redes": {
            "Facebook": "https://facebook.com/dulcerialilis",
            "Instagram": "https://instagram.com/dulcerialilis"
        }
    }
    return render(request, "catalogo/empresa.html", data)
