from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'Tiendalibre/home.html', {})

def sobremi(request):
    return render(request, 'Tiendalibre/sobremi.html', {})