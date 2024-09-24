# Gestionar vehiculos para una aplicación de alquiler
class Vehiculo:
    def __init__(self, tipo, marca, modelo, anio):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def obtener_info(self):
        return f'Vehiculo: {self.marca} {self.modelo} {self.anio}'


auto = Vehiculo('Auto', 'Toyota', 'Corolla', 2020)
print(auto.obtener_info())

moto = Vehiculo('Motocicleta', 'Honda', 'CBR', 2021)
print(moto.obtener_info())
