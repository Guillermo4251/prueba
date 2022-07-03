from operator import index
from turtle import home
from django.urls import path
from .views import *

urlpatterns = [
     path('Index', Index, name="Index"),
     path('InicioSesion', InicioSesion, name="InicioSesion"),
     path('Regist', Regist, name="Regist"),
     path('CarritoCompras', CarritoCompras, name="CarritoCompras"),
     path('CarritoComprasHistorial', CarritoComprasHistorial, name="CarritoComprasHistorial"),
     path('IniciosesionAdmin', IniciosesionAdmin, name="IniciosesionAdmin"),
     path('crudproductos', crudproductos, name="crudproductos"),
     path('crudProductos2', crudProductos2, name="crudProductos2"),
     path('Formulario', Formulario, name="Formulario"),
     path('FormularioEmp', FormularioEmp, name="FormularioEmp"),
     path('IndexDescuento', IndexDescuento, name="IndexDescuento"),
     path('Suscribirse', Suscribirse, name="Suscribirse"),
     path('Pago', Pago, name="Pago"),
     path('pagina', pagina, name="pagina"),
    
]
