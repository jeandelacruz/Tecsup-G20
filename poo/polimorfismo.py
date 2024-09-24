# Procesar pagos con diferentes metodos
class MetodoPago:
    def pagar(self):
        pass


class TarjetaCredito(MetodoPago):
    def pagar(self, monto):
        return f'Estas pagando {monto} con una tarjeta de credito'


class BilleteraDigital(MetodoPago):
    def pagar(self, monto):
        return f'Estas pagando {monto} con una billetera digital'


tarjeta_credito = TarjetaCredito()
print(tarjeta_credito.pagar(500))

billetera_digital = BilleteraDigital()
print(billetera_digital.pagar(120))
