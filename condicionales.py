# if -> ejecuta un bloque de codigo si la condición es verdadera
# else -> ejecuta un bloque de codigo si la condición anterior no es verdadera
# elif -> permite agregar mas condiciones en caso el primero no se cumpla

# Caso de uso 1
# Validar que el usuario sea mayor de edad (18 años).
edad = 16
if edad >= 18:
    print('Es mayor de edad !')
else:
    print('Es menor de edad !')

# Operador Ternario
# print('Es mayor de edad') if edad >= 18 else print('Es menor de edad')

# Caso de uso 2
# Validar el clima, para poder decidir si llevar un paragua o no
clima = "soleado"

if clima == "lloviendo":
    print("Llevar un paraguas")
elif clima == "nublado":
    print("Lleva un paraguas por si acaso")
else:
    print("No necesito paraguas")
