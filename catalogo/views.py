from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Diccionario de categorías
CATEGORIAS = [
    "Chocolates",
    "Galletas",
    "Alfajores",
    "Confiteria",
    "Bomboneria"
]

# Diccionario de productos por categoría
PRODUCTOS = {
    "Alfajores": ["Alfajor de papaya", "Alfajor de nuez", "Alfajor vegano"],
    "Chocolates": ["Chocolate bitter", "Chocolate con almendras", "Chocolate blanco"],
    "Galletas": ["Galleta de avena", "Galleta chips", "Galleta de mantequilla"],
    "Confiteria": ["Calugas de manjar de cabra", "Cuchuflí chocolate", "Gomitas frutales"],
    "Bomboneria": ["Bombón frutilla", "Bombón trufa", "Bombón café"]
}

# Diccionario de detalles por producto
DETALLES ={
    "Chocolate bitter": {
        "descripcion": "Chocolate amargo 70% cacao.",
        "ingredientes": "Cacao, manteca de cacao, azúcar.",
        "tiempo_produccion": "2 horas",
        "imagen": "chocolate_bitter.jpg"
    },
    "Chocolate con almendras": {
        "descripcion": "Chocolate con trozos de almendras chilenas.",
        "ingredientes": "Cacao, almendras, leche, azúcar.",
        "tiempo_produccion": "2 horas",
        "imagen": "chocolate_almendras.jpg"
    },
    "Chocolate blanco": {
        "descripcion": "Chocolate blanco artesanal.",
        "ingredientes": "Manteca de cacao, leche, azúcar.",
        "tiempo_produccion": "1.5 horas",
        "imagen": "chocolate_blanco.jpg"
    },
    "Galleta de avena": {
        "descripcion": "Galleta casera de avena con pasas.",
        "ingredientes": "Avena, pasas, harina, huevo, azúcar.",
        "tiempo_produccion": "40 minutos",
        "imagen": "galleta_avena.jpg"
    },
    "Galleta chips": {
        "descripcion": "Galleta de mantequilla con chips de chocolate.",
        "ingredientes": "Harina, mantequilla, azúcar, chips de chocolate.",
        "tiempo_produccion": "35 minutos",
        "imagen": "galleta_chips.jpg"
    },
    "Galleta de mantequilla": {
        "descripcion": "Clásica galleta de mantequilla.",
        "ingredientes": "Harina, mantequilla, azúcar.",
        "tiempo_produccion": "30 minutos",
        "imagen": "galleta_mantequilla.jpg"
    },
    "Bombón frutilla": {
        "descripcion": "Bombón relleno de crema de frutilla.",
        "ingredientes": "Chocolate, frutilla, leche.",
        "tiempo_produccion": "1 hora",
        "imagen": "bombon_frutilla.jpg"
    },
    "Bombón trufa": {
        "descripcion": "Bombón relleno de ganache de chocolate.",
        "ingredientes": "Chocolate, crema, cacao en polvo.",
        "tiempo_produccion": "1 hora",
        "imagen": "bombon_trufa.jpg"
    },
    "Bombón café": {
        "descripcion": "Bombón con relleno de café.",
        "ingredientes": "Chocolate, café, crema, azúcar.",
        "tiempo_produccion": "1 hora",
        "imagen": "bombon_cafe.jpg"
    },
    "Alfajor de papaya": {
        "descripcion": "Alfajor relleno con papaya chilena.",
        "ingredientes": "Harina, huevo, papaya, azúcar, leche.",
        "tiempo_produccion": "2 horas",
        "imagen": "alfajor_papaya.jpg"
    },
    "Calugas de manjar de cabra": {
        "descripcion": "Dulces de leche de cabra con caramelo.",
        "ingredientes": "Leche de cabra, azúcar, mantequilla.",
        "tiempo_produccion": "1.5 horas",
        "imagen": "calugas.jpg"
    },
    "Alfajor de nuez": {
        "descripcion": "Alfajor relleno con crema de nuez chilena.",
        "ingredientes": "Harina, huevo, nueces, azúcar, leche condensada.",
        "tiempo_produccion": "2.5 horas",
        "imagen": "alfajor_nuez.jpg"
    },
    "Alfajor vegano": {
        "descripcion": "Alfajor sin productos de origen animal, relleno de manjar vegano.",
        "ingredientes": "Harina de almendras, leche de coco, endulzante natural, cacao.",
        "tiempo_produccion": "3 horas",
        "imagen": "alfajor_vegano.jpg"
    },
    "Cuchuflí chocolate": {
        "descripcion": "Cuchuflí relleno de chocolate artesanal.",
        "ingredientes": "Harina, huevo, chocolate, azúcar, vainilla.",
        "tiempo_produccion": "1 hora",
        "imagen": "cuchufli.jpg"
    },
    "Gomitas frutales": {
        "descripcion": "Gomitas suaves con sabores frutales naturales.",
        "ingredientes": "Gelatina, jugo de frutas natural, azúcar, colorantes vegetales.",
        "tiempo_produccion": "45 minutos",
        "imagen": "gomitas.jpg"
    }
}


# Vista landing page
def landing(request):
    return render(request, 'catalogo/landing.html')

# Vista catálogo principal
def catalogo(request):
    return render(request, 'catalogo/catalogo.html', {
        "categorias": CATEGORIAS
    })

# Vista subcatálogo
def subcatalogo(request, categoria):
    productos = PRODUCTOS.get(categoria, [])
    productos_con_detalle = []

    for p in productos:
        detalle = DETALLES.get(p, {})
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
    detalle = DETALLES.get(producto, {})
    categoria = None
    for cat, prods in PRODUCTOS.items():
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
