nombre = input("Introduce tu nombre: ")

# Convertir el nombre a mayúsculas
nombre_mayusculas = nombre.upper()

numero_letras = len(nombre.replace(" ", ""))
print(f"{nombre_mayusculas} tiene {numero_letras} letras.")
