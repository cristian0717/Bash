from django.db import models

class Login (models.Model):
    usuario = models.CharField(max_length=15)
    contraseña = models.IntegerField()

class Ventas (models.Model):
    articulo = models.CharField(max_length=50)
    codigo = models.CharField(max_length=15)
    precio = models.IntegerField()
    cantidad = models.IntegerField()

    def __str__ (self):
        return self.codigo + " " + str(self.cantidad)

class MediosDePago(models.Model):
    tarjeta = models.IntegerField()
    mercado_pago = models.IntegerField()
    efectivo = models.IntegerField()
    transferencia = models.IntegerField()


class Cliente (models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    dni = models.IntegerField()
    tipo_de_factura = models.CharField(max_length=10)

    def __str__ (self):
        return self.apellido + " " + str(self.dni)

class Articulo (models.Model):
    codigo = models.CharField (max_length=12)
    descripcion = models.CharField(max_length=40)
    rubro = models.CharField(max_length=15)
    precio = models.IntegerField()

    def __str__ (self):
        return self.descripcion

class Vendedor (models.Model):
    nombre = models.CharField (max_length=15)
    apellido = models.CharField (max_length=15)
    numero_vendedor = models.IntegerField()


    def __str__ (self):
        return self.nombre + " " + str(self.numero_vendedor)
