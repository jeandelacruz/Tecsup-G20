# Ejercicio 1
'''
1. Crear una clase Calculadora.
2. La calculado debe tener metodos para realizar las operaciones suma, resta, multiplicacion y division.
3. El usuario debera ingresar 2 números (float), y luego seleccionar la operacion que desea realizar.
4. Mostrar el resultado final: La {operacion} de los numeros: {n1}, {n2} da como resultado: {resultado}
'''


# class Calculadora:
#     def __init__(self, numero_uno, numero_dos):
#         self.numero_uno = numero_uno
#         self.numero_dos = numero_dos

#     def sumar(self):
#         return self.numero_uno + self.numero_dos

#     def restar(self):
#         return self.numero_uno - self.numero_dos

#     def multiplicar(self):
#         return self.numero_uno * self.numero_dos

#     def dividir(self):
#         if self.numero_dos != 0:
#             return self.numero_uno / self.numero_dos
#         else:
#             return 'No se puede dividir por 0'


# numero_uno = float(input('Ingrese el primer numero: '))
# numero_dos = float(input('Ingrese el segundo numero: '))
# operacion = input(
#     'Ingrese la operación (sumar, restar, multiplicar, dividir): '
# )

# calculadora = Calculadora(numero_uno, numero_dos)

# if operacion == 'sumar':
#     resultado = calculadora.sumar()
# elif operacion == 'restar':
#     resultado = calculadora.restar()
# elif operacion == 'multiplicar':
#     resultado = calculadora.multiplicar()
# elif operacion == 'dividir':
#     resultado = calculadora.dividir()
# else:
#     resultado = 'Operación no valida'


# print(
#     f'El resultado de {operacion} {numero_uno} y {numero_dos} es: {resultado}'
# )

# Ejercicio 2
'''
1. Crear una clase Tareas que administre una lista de tareas pendientes.
2. El usuario podrá agregar, eliminar y ver tareas.
3. Utilizar input para permitir que el usuario realice las acciones.
4. Utilizar while, para que el programa se siga ejecutando hasta que el usuario decida salir.
5. Mostrar las tareas con un salto de linea, usando f-string.
'''


class Tareas:
    def __init__(self):
        self.lista_tareas = []

    def agregar_tarea(self, tarea):
        self.lista_tareas.append(tarea)

    def eliminar_tarea(self, tarea):
        if tarea in self.lista_tareas:
            self.lista_tareas.remove(tarea)
            return f'La tarea {tarea} se elimino con exito'
        else:
            return 'La tarea no existe'

    def mostrar_tareas(self):
        if len(self.lista_tareas) == 0:
            return 'No hay tareas registradas'
        else:
            resultado = ''
            for tarea in self.lista_tareas:
                resultado += f'{tarea}\n'
            return resultado


tareas = Tareas()

while True:
    print('''
    1. Agregar tarea
    2. Eliminar tarea
    3. Ver tareas
    4. Salir
    ''')

    opcion = input('Seleccione una opcion: ')

    if opcion == '1':
        nueva_tarea = input('Ingrese la nueva tarea: ')
        tareas.agregar_tarea(nueva_tarea)
        print(f'Tarea {nueva_tarea} se registro con exito')
    elif opcion == '2':
        tarea_eliminar = input('Ingrese la tarea a eliminar: ')
        resultado = tareas.eliminar_tarea(tarea_eliminar)
        print(resultado)
    elif opcion == '3':
        print('Tareas registradas: ')
        print(tareas.mostrar_tareas())
    elif opcion == '4':
        print('Saliendo del programa')
        break
    else:
        print('Opcion no valida, intente nuevamente')
