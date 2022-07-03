from collections import UserDict, UserList
from site import USER_BASE
from django.db import models

# Create your models here.


class sub(models.Model):
    idSub = models.CharField(primary_key=True , max_length=30)
    usuario=models.CharField(max_length=30)
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)

    def str(self) -> str:
        return self.nombre

class Producto(models.Model):
    IdProducto = models.CharField(primary_key=True, max_length=30 )
    NombreProducto = models.CharField(max_length=30)
    Valor = models.IntegerField()
    stock = models.IntegerField()
    descuento = models.IntegerField()


    def str(self) -> str:
        return self.NombreProducto

class compra(models.Model):
    Idcompra = models.CharField(primary_key=True , max_length=40 )
    usuario=models.CharField(max_length=30)
    fechaEnvio = models.DateField()
    fechaEstimada = models.DateField()
    fechaEntrega = models.DateField()
    def str(self) -> str:
        return self.Idcompra

class venta(models.Model):
    IdVenta = models.CharField(primary_key=True , max_length=30)
    idCompra=models.ForeignKey(compra,on_delete=models.CASCADE)
    idProducto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad= models.IntegerField()
    def str(self) -> str:
        return self.IdVenta