# function nombre() {} -> Javascript

# def nombreFuncion():
#    pass

# Función con parametro
def saludar(nombre):
    print(f'Hola {nombre}, como estas?')


# Función con parametros, y asignarlos valores por defecto
def saludarConNombreCompleto(apellido, nombre="Bruno"):
    print(f'Hola {nombre} {apellido}')


# saludarConNombreCompleto(nombre="Diego", apellido="Hernandez")

# Ejercicio
# Crear una función que reciba 2 números, donde el primer número tendra un valor por defecto: 10
# Si la suma de ambos es un número par, mostrar la mitad de dicha suma
# y si no es par, mostramos el resultado de dicha suma
def ejercicioUno(n_dos, n_uno=10):
    suma = n_uno + n_dos
    if suma % 2 == 0:
        print(suma / 2)
    else:
        print(suma)


# Multiparametros
# Signos (* - **)
# *args -> nos permite recibir parametros infinitos
def alumnosInscritos(*args):
    print(args)

# alumnosInscritos("Bruno", "Brayan", "Daniel", "Diego", "Guiovany")


# **kwargs -> nos permite recibir parametros infinitos
def cursosDeAlumnos(**kwargs):
    print(kwargs)


# cursosDeAlumnos(curso_uno="Algebra", curso_dos="Aritmetica",
#                curso_tres="Matematica")

# Ejercicio 2
# Crea una función que reciba N notas, y nos indique cuantas fueron desaprobadas y cuantas aprobadas
# nota > 13 -> Aprobado
def ejercicioDos(*args):
    aprobados = 0
    desaprobados = 0

    for nota in args:
        if nota > 13:
            aprobados += 1
        else:
            desaprobados += 1

    print(f'Aprobados -> {aprobados}')
    print(f'Desaprobados -> {desaprobados}')


# ejercicioDos(10, 16, 18, 13, 5)
