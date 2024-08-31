# Solicitar al usuario que ingrese el precio del producto
precio = input("Introduce el precio del producto en euros (ejemplo: 12.34): ")

euros, centimos = precio.split('.')
print("Número de euros:", euros)
print("Número de céntimos:", centimos)
