# Solicitar al usuario que ingrese una frase
frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal: ")

vocal = vocal.lower()

frase_modificada = frase.replace(vocal, vocal.upper())
print("La frase con la vocal en mayúscula es:", frase_modificada)
