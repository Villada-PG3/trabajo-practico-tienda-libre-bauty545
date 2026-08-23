from django.shortcuts import render
from .models import Producto

def home(request):
    productos = Producto.objects.all()

    contexto = {
        "productos": productos
    }

    return render(request, "Tiendalibre/home.html", contexto)
    
def sobremi(request):
    return render(request, 'Tiendalibre/sobremi.html', {})