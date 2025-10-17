from django.shortcuts import render, get_object_or_404, redirect
from catalogo.models import Categoria, Producto
from catalogo.forms import ProductoForm
from django.http import HttpResponse


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



#####MANTENEDORES####
def mantenedores(request):
    return render(request, 'mantenedores/inicioMantenedores.html')



#Mantenedor productos 
def MantenedorAgregarProducto(request):
    form=ProductoForm()
    return render(request,'mantenedores/productos/MantenedorAgregarProducto.html',{'form':form})

def mostrar_todos_productos(request):
    productos = Producto.objects.all()
    return render(request, 'mantenedores/productos/todos_productos.html', {'productos': productos})


def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)

            if not producto.imagen or producto.imagen.strip() == "":
                producto.imagen = "default.jpg"

            producto.save()
            return redirect("mostrar_todos_productos")
       
    else:
        form = ProductoForm()

    return render(request, 'mantenedores/productos/MantenedorAgregarProducto.html', {'form': form})

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("mostrar_todos_productos")
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'mantenedores/productos/mantenedorEditarProducto.html', {'form': form, 'producto': producto})


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('mostrar_todos_productos')
    return render(request, 'mantenedores/confirmar_eliminacion.html', {'producto': producto})