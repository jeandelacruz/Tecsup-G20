# Jerarquia de empleados de una empresa

# Clase padre
class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def obtener_datos(self):
        return f'{self.nombre} tiene un sueldo de {self.sueldo}'


# Clase hijo
class Gerente(Empleado):
    def __init__(self, nombre, sueldo, area):
        super().__init__(nombre, sueldo)
        self.area = area

    def obtener_datos(self):
        return f'{self.nombre} es gerente del area {self.area} con un sueldo de {self.sueldo}'


empleado = Empleado('Ana', 3000)
print(empleado.obtener_datos())

gerente = Gerente('Sofia', 6800, 'Ventas')
print(gerente.obtener_datos())
