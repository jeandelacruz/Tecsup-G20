# Ejercicio 1
# Crea una estructura de datos, que me ayude a almacenar nombres de usuarios
# Donde me imprima el usuario de la posición 4

# nombre_uno = input('Ingresa el primer nombre: ')
# nombre_dos = input('Ingresa el segundo nombre: ')
# nombre_tres = input('Ingresa el tercer nombre: ')
# nombre_cuatro = input('Ingresa el cuarto nombre: ')

# usuarios = [nombre_uno, nombre_dos, nombre_tres, nombre_cuatro]

# print(f'usuarios -> {usuarios}')
# print(f'posicion 4 -> {usuarios[3]}')


# Ejercicio 2
# Crea una estructura de datos, que me ayude a almacenar los datos de contacto de un usuario
# Debe si o si, tener el telefono, direccion y dni
# Utilizamos un diccionario
telefono = input('Ingrese el telefono del contacto: ')
direccion = input('Ingrese la direccion del contacto: ')
dni = int(input('Ingrese el DNI del contacto: '))

contacto = {
    'telefono': telefono,
    'direccion': direccion,
    'dni': dni
}

print(f'Datos de Contacto -> {contacto}')


# Ejercicio 3
# Crea una estructura de datos, que me ayude a almacenar coordenadas
# Las coordenadas deben ser (x, y), de un plano cartesiano
# Luego mostrar las coordenadas, con sus puntos x e y.
# coordenada = (40.7128, -74.0060)
# print(f'Coordenada X {coordenada[0]} - Coordenada Y {coordenada[1]}')
