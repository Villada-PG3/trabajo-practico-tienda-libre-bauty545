from django.shortcuts import render, get_object_or_404
from .models import Producto
from random import random

def home(request):
    productos = Producto.objects.all()[:3]
    
    context = {
        'titulo': '🎸 Tienda de instrumentos musicales',
        'productos_destacados': productos,
        'usuario_logueado': random() < 0.80,  # Simulación de usuario logueado o no
    }

    return render(request, "Tiendalibre/home.html", context)
    
def sobremi(request):
    return render(request, 'Tiendalibre/sobremi.html', {})

def catalogo(request):
    productos = Producto.objects.all()
    context = {
        'titulo': 'Catálogo de productos',
        'productos': productos,
    }
    return render(request, 'Tiendalibre/catalogo.html', context)

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    context = {
        'titulo': producto.nombre,
        'producto': producto,
    }
    return render(request, 'Tiendalibre/detalle_producto.html', context)
