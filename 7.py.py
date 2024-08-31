# Solicitar al usuario que ingrese su correo electrónico
correo = input("Introduce tu correo electrónico: ")
nombre_usuario = correo.split('@')[0]

nuevo_correo = nombre_usuario + "@ceu.es"
print("Tu nuevo correo electrónico es:", nuevo_correo)
