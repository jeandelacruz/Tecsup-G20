# Operadores Matematicos (Aritmeticos)
# Suma (+)
numero_1 = 10
numero_2 = 5
suma = numero_1 + numero_2
# La suma de 10 y 5 es: 15
# f-string
# print("La suma de " + str(numero_1) + " y " +
#       str(numero_2) + " es: " + str(suma))
print(f'La suma de {numero_1} y {numero_2} es: {suma}')

# Resta (-)
numero_3 = 5
numero_4 = 2
resta = numero_3 - numero_4
print(f'La resta de {numero_3} y {numero_4} es: {resta}')

# Multiplicación (*)
numero_5 = 5
numero_6 = 10
multiplicacion = numero_5 * numero_6
print(f'La multiplicacion de {numero_5} y {numero_6} es: {multiplicacion}')

# Potencias (**)
numero_7 = 3
potencia_al_cubo = numero_7 ** 3
print(f'La potencia al cubo de {numero_7} es: {potencia_al_cubo}')

# Residuo (%)
numero_8 = 24
numero_9 = 7
residuo = numero_8 % numero_9
print(f'El residuo de {numero_8} y {numero_9} es: {residuo}')

# División Entera (/) -> Flotante (Decimal)
numero_10 = 12
numero_11 = 5
division = numero_10 / numero_11
print(f'La multiplicacion de {numero_10} y {numero_11} es: {division}')

# Division Exacta (//) -> Redondear Hacia Abajo
division_exacta = numero_10 // numero_11
print(f'La division exacta de {numero_10} y {numero_11} es: {division_exacta}')
