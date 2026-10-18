from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import Producto

class HomeView(TemplateView):
    template_name = "Tiendalibre/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["titulo"] = "Productos destacados"
        context["productos_destacados"] = Producto.objects.all()[:6]

        return context
    
def sobremi(request):
    return render(request, 'Tiendalibre/sobremi.html', {})

class CatalogoView(ListView):
    model = Producto
    template_name = 'Tiendalibre/catalogo.html'
    context_object_name = 'productos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Catálogo de productos'
        return context

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    context = {
        'titulo': producto.nombre,
        'producto': producto,
    }
    return render(request, 'Tiendalibre/detalle_producto.html', context)
