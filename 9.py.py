# Solicitar al usuario que ingrese su fecha de nacimiento
fecha_nacimiento = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")

dia, mes, año = fecha_nacimiento.split('/')

print("Día:", dia.zfill(2))   
print("Mes:", mes.zfill(2))   
print("Año:", año)
