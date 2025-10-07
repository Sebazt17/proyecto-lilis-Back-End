from django.db import models
from django.utils import timezone
from .choices import TIPO_PROVEEDOR, ESTADO_PROVEEDOR, EVALUACION_CALIDAD

class Region(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre Región')
    codigo = models.CharField(max_length=5, verbose_name='Código Región', unique=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'region'
        verbose_name = 'Región'
        verbose_name_plural = 'Regiones'
        ordering = ['nombre']

class Proveedor(models.Model):
    razon_social = models.CharField(max_length=100, verbose_name='Razón Social')
    rut = models.CharField(max_length=12, verbose_name='RUT', unique=True)
    nombre_ficticio = models.CharField(max_length=100, verbose_name='Nombre Ficticio Empresa')
    direccion = models.CharField(max_length=200, verbose_name='Dirección')
    telefono = models.CharField(max_length=15, verbose_name='Teléfono')
    email = models.EmailField(verbose_name='Correo Electrónico')
    tipo_proveedor = models.CharField(max_length=2, choices=TIPO_PROVEEDOR, verbose_name='Tipo de Proveedor')
    estado = models.CharField(max_length=1, choices=ESTADO_PROVEEDOR, default='A', verbose_name='Estado')
    fecha_registro = models.DateTimeField(default=timezone.now, verbose_name='Fecha de Registro')
    region = models.ForeignKey(Region, null=False, on_delete=models.CASCADE, related_name="proveedores", verbose_name='Región')
    productos_que_abastece = models.TextField(max_length=500, verbose_name='Productos que Abastece')
    tiempo_entrega_promedio = models.IntegerField(verbose_name='Tiempo de Entrega (días)')
    certificaciones = models.TextField(max_length=300, blank=True, verbose_name='Certificaciones')
    evaluacion_calidad = models.IntegerField(choices=EVALUACION_CALIDAD, default=3, verbose_name='Evaluación de Calidad')

    def __str__(self):
        return f"{self.razon_social} - {self.get_tipo_proveedor_display()}"
    
    class Meta:
        db_table = 'proveedor'
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['razon_social']