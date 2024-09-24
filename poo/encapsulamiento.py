# Gestión de cuentas bancarias
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, monto):
        self.__saldo += monto

    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto

    def obtener_saldo(self):
        # Validar contraseña o palabra secreta
        return self.__saldo


cuenta_uno = CuentaBancaria('Cristian Elvis', 1800)
print(f'El saldo actual: {cuenta_uno.obtener_saldo()}')
cuenta_uno.depositar(500)
print(f'Saldo despues del deposito: {cuenta_uno.obtener_saldo()}')
cuenta_uno.retirar(1300)
print(f'Saldo despues del retiro: {cuenta_uno.obtener_saldo()}')
