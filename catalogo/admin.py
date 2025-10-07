from django.contrib import admin
from catalogo.models import Categoria,Producto
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre']
    search_fields = ['nombre']
    ordering = ['nombre']

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','ingredientes',
                    'tiempo_produccion','descripcion',
                    'imagen','categoria']
    list_filter = ['categoria']
    search_fields = ['nombre', 'descripcion']
    
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Producto,ProductoAdmin)