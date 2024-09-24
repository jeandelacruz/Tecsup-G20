# try catch -> javascript
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print(resultado)
except TypeError:
    print('Ocurrio un error, al convertir el dato en entero.')
except ValueError:
    print('Ocurrio un error, el valor ingresado es un texto, debe usarse un número')
except Exception as e:
    print(e.__class__, e)
    print('Ocurrio un error, comunicate con soporte.')
else:  # se va a ejecutar o mostrar, cuando no haya un error
    print(f'No hubo un error -> {resultado}')
finally:  # se va a ejecutar o mostrar, aunque haya o no haya error
    print('Siempre')
