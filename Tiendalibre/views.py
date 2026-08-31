from django.shortcuts import render
from .models import Producto

def home(request):
    productos = Producto.objects.all()

    productos_destacados = [
        {'nombre': 'Piano', 'precio': 1000, 'stock': 10},
        {'nombre': 'Guitarra acústica', 'precio': 350, 'stock': 67},
        {'nombre': 'Batería', 'precio': 800, 'stock': 23},
        {'nombre': 'Violín', 'precio': 450, 'stock': 0},
        {'nombre': 'Teclado musical', 'precio': 600, 'stock': 0},
        {'nombre': 'Saxofón', 'precio': 700, 'stock': 11},
        {'nombre': 'Ukelele', 'precio': 120, 'stock': 10},
    ]

    context = {
        'titulo': 'Tienda de instrumentos musicales',
        'productos_destacados': productos_destacados,
        'usuario_logueado': True
    }

    return render(request, "Tiendalibre/home.html", context)
    
def sobremi(request):
    return render(request, 'Tiendalibre/sobremi.html', {})