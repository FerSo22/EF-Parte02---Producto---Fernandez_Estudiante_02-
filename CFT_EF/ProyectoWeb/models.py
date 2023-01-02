from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.TextField(max_length = 4)
    nombre = models.TextField(max_length = 80)
    precio_compra = models.FloatField()
    precio_venta = models.FloatField()
    fecha_compra = models.DateField(auto_now = False)
    facha_registro = models.DateField(auto_now_add = True)
    estado = models.TextField(max_length = 1)