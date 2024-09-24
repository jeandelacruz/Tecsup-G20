# Caso de uso
# Creando una aplicacion para gestionar alumnos en una escuela.
# En el cual debemos almacenar información de los mismos.
# Las cuales pueden ser sus notas, clases, horarios, etc.
# - Una lista de alumnos, que esten registrados.
# - Un diccionario que asocie el alumno con sus notas.
# - Una tupla que almacene el horario del alumno.

# Lista ([]) Alt 91 ([) - Alt 93 (]) - list()
# Estructura de datos Mutable
# Indice - Posición (n-1)
# mi_lista = [1, 2, 3, 'hola', True]
# print(f'Primer valor de la lista: {mi_lista[0]}')
# print(f'Cuarto valor de la lista: {mi_lista[3]}')

personas = ['Alan', 'Cristian', 'Eduardo']
print(f'inicio -> {personas}')

# Funciones
# append -> agregar un valor a la lista (se añade al final)
personas.append('Daniel')
print(f'append -> {personas}')

# insert -> agregar un valor a la lista, pero indicandole su indice
personas.insert(0, 'Jesus')
print(f'insert -> {personas}')

# extend -> unir 2 listas
personas_nuevas = ['Fritz', 'Hugo', 'Juan']
personas.extend(personas_nuevas)
print(f'extend -> {personas}')

# remove -> elimina un valor de la lista
personas.remove('Daniel')
print(f'remove -> {personas}')

# pop -> eliminar un valor de la lista, mediante su indice
personas.pop(5)
print(f'pop -> {personas}')

# sort -> ordenar los valores de una lista
# reverse=False -> menor a mayor (no es necesario definirlo)
# reverse=True -> mayor a menor
personas.sort(reverse=False)
print(f'sort -> {personas}')

# len -> cuenta los elementos de una secuencia (estructura de datos o string)
print(f'Total de personas: {len(personas)}')
