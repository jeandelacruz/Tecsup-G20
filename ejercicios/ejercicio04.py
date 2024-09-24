# Ejercicio 1
# Solicitar una palabra y debemos de validar si es un palindromo o no.
# ana -> ana
########################
# string subconjuntos - slicing
palabra = "aeropuerto"
# string[0:len(string):1]
# print(palabra[::-1])

# for e insert
# letras_invertidas = []
#
# for letra in palabra:
#    letras_invertidas.insert(0, letra)
#
# print("".join(letras_invertidas))

# join (str) y reversed
# print("".join(reversed(palabra)))

# Ejercicio 2
# Solicitar el año en el que nacimos, este mismo se va a iterar restandolo el año actual
# de tal manera nos mostraria los mensajes como :
# En 1995 tenias 1 años
# En 1996 tenias 2 años
# .....................
# Condiciones:
# El año ingresado no debe ser mayor al año actual
# Cuando se llegue al año actual, el mensaje debe decir: Actualmente en el año 2022, tienes 28 años

anio_actual = 2022
anio_nacimiento = int(input("Ingrese el año de nacimiento: "))

if anio_nacimiento < anio_actual:
    edad = anio_actual - anio_nacimiento
    for value in range(edad):
        edad_anterior = value + 1
        message = f'En el año {anio_nacimiento + edad_anterior} tenias {edad_anterior} años'
        if anio_nacimiento + edad_anterior == anio_actual:
            message = f'Actualmente en el año {anio_actual}, tienes {edad_anterior} años'
        print(message)
else:
    print(f'El año de nacimiento no debe ser mayor a {anio_actual}')
