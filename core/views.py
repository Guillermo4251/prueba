from distutils import core
from .models import *
from django .shortcuts import render

def Index (request):
    return render (request, 'core/Index.html')
    
def InicioSesion(request):
    return render (request, 'core/InicioSesion.html')

def Regist(request):
    return render (request, 'core/Regist.html')

def CarritoCompras(request):
    return render (request, 'core/CarritoCompras.html')

def CarritoComprasHistorial(request):
    return render (request, 'core/CarritoComprasHistorial.html')

def IniciosesionAdmin(request):
    return render (request, 'core/IniciosesionAdmin.html')

def crudproductos(request):
    return render (request, 'core/crudproductos.html')

def crudProductos2(request):
    return render (request, 'core/crudProductos2.html')

def Formulario(request):
    return render (request, 'core/Formulario.html')

def FormularioEmp(request):
    return render (request, 'core/FormularioEmp.html')

def IndexDescuento(request):
    return render (request, 'core/IndexDescuentos.html')

def Suscribirse(request):
    return render (request, 'core/Suscribirse.html')

def Pago(request):
    return render (request, 'core/Pago.html')

def pagina (request):
    return render (request, 'core/pagina.html')