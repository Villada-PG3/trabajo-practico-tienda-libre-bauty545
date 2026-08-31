from django.shortcuts import render
from .models import Producto

def home(request):
    productos = Producto.objects.all()

    productos_destacados = [
        {'nombre': 'Piano', 'precio': 1000, 'stock': 10, 'descripcion': 'Instrumento de teclas clásico y elegante'},
        {'nombre': 'Guitarra acústica', 'precio': 350, 'stock': 67, 'descripcion': 'Sonido cálido y resonante perfecto para principiantes'},
        {'nombre': 'Batería', 'precio': 800, 'stock': 0, 'descripcion': 'Conjunto completo de percusión profesional'},
        {'nombre': 'Violín', 'precio': 450, 'stock': 23, 'descripcion': 'Instrumento de cuerda de sonido dulce'},
        {'nombre': 'Saxofón', 'precio': 700, 'stock': 11, 'descripcion': 'Instrumento de viento metálico de jazz'},
        {'nombre': 'Ukelele', 'precio': 120, 'stock': 0, 'descripcion': 'Pequeña guitarra hawaiana fácil de tocar'},
        {'nombre': 'None', 'precio': None, 'stock': 0, 'descripcion': 'None'},
    ]

    context = {
        'titulo': '🎸 Tienda de instrumentos musicales',
        'productos_destacados': productos_destacados,
        'usuario_logueado': True
    }

    return render(request, "Tiendalibre/home.html", context)
    
def sobremi(request):
    return render(request, 'Tiendalibre/sobremi.html', {})