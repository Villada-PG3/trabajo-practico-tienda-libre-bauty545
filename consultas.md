- from tiendalibre.models import Producto, Categoria #importar productos
1. Producto.objects.all() #Trae todos los productos
2. Producto.objects.count() #Cuenta la cantidad de productos
3. Producto.objects.order_by("-nombre") #Trae los productos en el orden inverso al alfabeto
4. Producto.objects.filter(stock=0) #Trae los productos sin stock
5. Producto.objects.filter(stock__gt=20) #Trae los productos que tengan stock > 20
6. Producto.objects.get(id=20) #Trae el product con la ID #20
7. Producto.objects.filter(categoria__nombre__icontains="Electronica") #Todos los productos que su categoria contenga la palabra Electronica.
8. Producto.objects.filter(nombre__icontains="pelota") #Todos los productos que contengan el nombre "pelota".
9. Producto.objects.filter(stock__gte=23) #Todos los productos que tengan stock mayor o igual a 23
10. categoria = Categoria.objects.first()
    categoria.productos.all() #Busca la primer categoria, la define con el nombre "categoria" y llama a todos los productos relacionados con esa categoria.