from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from catalogo import models as infoProductos


# Vista landing page
def landing(request):
    return render(request, 'catalogo/landing.html')

# Vista catálogo principal
def catalogo(request):
    return render(request, 'catalogo/catalogo.html', {
        "categorias": infoProductos.CATEGORIAS
    })

# Vista subcatálogo
def subcatalogo(request, categoria):
    productos = infoProductos.PRODUCTOS.get(categoria, [])
    productos_con_detalle = []

    for p in productos:
        detalle = infoProductos.DETALLES.get(p, {})
        productos_con_detalle.append({
            "nombre": p,
            "imagen": detalle.get("imagen", "default.jpg")
        })

    return render(request, "catalogo/subcatalogo.html", {
        "categoria": categoria,
        "productos": productos_con_detalle
    })


# Vista detalle
def detalle_producto(request, producto):
    detalle = infoProductos.DETALLES.get(producto, {})
    categoria = None
    for cat, prods in infoProductos.PRODUCTOS.items():
        if producto in prods:
            categoria = cat
            break
    return render(request, "catalogo/detalle.html", {"producto": producto, "detalle": detalle, "categoria": categoria})

# Vista empresa (misión, visión, valores, etc.)
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