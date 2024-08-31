# Pedir el número de teléfono
telefono = input("Introduce un número de teléfono en el formato +34-número-extensión: ")

partes = telefono.split("-")

numero_sin_prefijo_y_extension = partes[1]

print(f"El número de teléfono sin el prefijo y la extensión es: {numero_sin_prefijo_y_extension}")
