from django.contrib import admin
from proveedores.models import Region, Proveedor

class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'codigo']
    search_fields = ['nombre', 'codigo']
    ordering = ['nombre']

class ProveedorAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'razon_social', 
        'rut', 
        'nombre_ficticio',  
        'tipo_proveedor', 
        'region', 
        'estado'
    ]
    list_filter = ['tipo_proveedor', 'estado', 'region']
    search_fields = ['razon_social', 'rut', 'nombre_ficticio']  
    
admin.site.register(Region, RegionAdmin)
admin.site.register(Proveedor, ProveedorAdmin)