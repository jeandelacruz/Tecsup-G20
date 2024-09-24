# Ejercicio 1
# Validar la hora (hh) 24 hrs, en la cual:
# Si son mas de las 6 am, me muestre el mensaje vamos a trabajar
# Si son las 12 pm, me muestre es hora de almorzar
# Si son las 6 pm, me muestre es hora de salir del trabajo
# Si son las 10 pm, me muestre es hora de dormir

# hora_actual = 18

# if hora_actual >= 6 and hora_actual < 12:
#     print('Vamos a trabajar')
# elif hora_actual == 12:
#     print('Hora de almorzar')
# elif hora_actual == 18:
#     print('Hora de salir del trabajo')
# elif hora_actual == 22:
#     print('Hora de dormir')

# Ejercicio 2
# Necesito crear una validación de entradas al cine
# Las variables que voy tener deben hacer referencia a:
# Mi dinero actual, Costo de la entrada y si soy miembro del cine
# Validar si cuento con el dinero, para la entrada del cine
# Pero si soy miembro, mi entrada es gratis
dinero = 100
costo_entrada = 20
es_miembro = True

if dinero >= costo_entrada or es_miembro:
    print('Puedo entrar al cine')
else:
    print('No tengo dinero suficiente, pipipi')
