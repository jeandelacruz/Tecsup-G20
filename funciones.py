# Sintaxis
# def nombre_funcion(parametros):
#     # Bloque de codigo
#     print(parametros) # Ejemplo
#     return resultado # Opcional

# Ejemplo 1
# Crear una función que imprima un saludo
# def saludar():
#     print('Hola, como estas?')


# saludar()


# Ejemplo 2
# Crear una funcion que reciba un nombre e imprima un saludo
# def saludar(nombre):
#     print(f'Hola, {nombre}, como estas?')


# saludar("Hugo")

# Ejemplo 3
# Crear una funcion que reciba un nombre y su apellido, e imprima un saludo
# Si no se envia el nombre, debe usar Eduardo por defecto
# Si no se envia el apellido, debe usar Medina por defecto
# TIP: Primero estan los parametros sin valor por defecto, seguido de los que si tienen
# valor por defecto.
# def saludar(nombre='Eduardo', apellidos='Medina', edad=0):
#     print(f'Hola, {nombre} {apellidos}, como estas?')


# saludar(apellidos='Alcantara', nombre='Juan')

# Multiples Parametros
# Crear una función que sume los valores que se envien como parametro
# 1er Caso - Simple usando listas
# def suma(numeros):
#     total = 0
#     for numero in numeros:
#         total += numero
#     return total


# resultado = suma([1, 3, 4, 5])
# print(resultado)

# 2do Caso - Empaquetado de parametros (*)
def suma(*numeros):
    # Tipo de dato: Tupla
    total = 0
    for numero in numeros:
        total += numero
    return total


resultado = suma(6, 4, 5, 13, 18, 55)
print(resultado)
