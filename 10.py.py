# Solicitar al usuario que ingrese los productos separados por comas
productos = input("Introduce los productos de la canasta de las compras, separados por comas: ")

lista_productos = productos.split(',')

for producto in lista_productos:
    print(producto.strip())  
