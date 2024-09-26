# Introducción a Flask

## ¿Qué es Flask?

Flask es un framework web minimalista escrito en Python que permite desarrollar aplicaciones web de forma rápida y sencilla. Es ideal para proyectos pequeños a medianos, aunque también puede ser escalable para proyectos más grandes.

Flask proporciona las herramientas necesarias para manejar peticiones HTTP, crear rutas, manejar parámetros en las URL y más. Es flexible y permite agregar diferentes módulos según lo necesites, como bases de datos, autenticación, etc.

## ¿Qué es HTTP y HTTPS?

**HTTP (HyperText Transfer Protocol)** es un protocolo que permite la comunicación entre un navegador y un servidor web. Las peticiones HTTP permiten que los usuarios soliciten recursos (como una página web o un archivo) desde un servidor.

**HTTPS (HTTP Secure)** es una versión segura de HTTP. Utiliza un protocolo de cifrado (SSL/TLS) para garantizar que la comunicación entre el cliente y el servidor esté protegida contra intercepciones o ataques.

### Beneficios de HTTPS

- Cifrado de los datos transmitidos.
- Protección contra ataques de intermediarios (MITM).
- Mejora la confianza de los usuarios y es valorado positivamente por motores de búsqueda como Google.

## Verbos HTTP

Los verbos HTTP son métodos que indican el tipo de acción que el cliente desea realizar en el servidor. Los más comunes son:

- **GET**: Se utiliza para obtener datos del servidor. Ideal para leer información sin realizar cambios.
- **POST**: Se utiliza para enviar datos al servidor, generalmente para crear o modificar recursos.
- **PUT**: Se utiliza para actualizar un recurso existente en el servidor.
- **DELETE**: Se utiliza para eliminar un recurso en el servidor.
- **PATCH**: Se utiliza para actualizar parcialmente un recurso existente.

### Cuándo usar cada verbo HTTP

- **GET**: Para solicitar datos, como obtener un perfil de usuario o una lista de productos.
- **POST**: Para enviar nuevos datos al servidor, como crear una nueva cuenta o agregar un producto al carrito de compras.
- **PUT**: Para actualizar datos completamente, como modificar toda la información de un usuario.
- **PATCH**: Para actualizar solo una parte de un recurso, como cambiar solo el correo electrónico de un usuario.
- **DELETE**: Para eliminar recursos, como borrar una cuenta de usuario o un producto del inventario.

## Codigos de Estado

De esta forma vamos a poder validar el resultado final de la solicitud realizada. Se agrupan en 5 categorias, pero solo utilizaremos 3:

#### 2xx: Exito

Indican que la solicitud recibida, se ha entendido y procesado correctamente.

- 200 OK
- 201 Created
- 204 No Content

#### 4xx: Errores del Cliente

Indican que el cliente ha cometido un error en la solicitud.

- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 405 Method Not Allowed

#### 5xx: Errores del Servidor

Indican que el servidor ha fallado.

- 500 Internal Server Error
- 502 Bad Gateway
- 503 Service Unavailable

## Creando Rutas en Flask

Las rutas en Flask son las URL que el servidor web va a escuchar. Cada ruta puede estar asociada con uno o más verbos HTTP.

### Ejemplo de rutas básicas

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenido a mi aplicación Flask"

@app.route('/about')
def about():
    return "Acerca de nosotros"
```

En este ejemplo, hemos creado dos rutas:

- /: Muestra un mensaje de bienvenida.
- /about: Muestra información sobre la aplicación.

### Usando Path Params

Los **Path Params** (parámetros de ruta) son parte de la URL que cambia dinámicamente. Se utilizan para identificar recursos específicos en el servidor.

#### Ejemplo con Path Params

```py
@app.route('/user/<username>')
def show_user_profile(username):
    return f'Perfil del usuario: {username}'
```

En este ejemplo, el parámetro `username` es dinámico y cambiará según el valor proporcionado en la URL. Si accedes a `/user/juan`, mostrará "Perfil del usuario: juan".

### Usando Query Params

Los **Query Params** son parámetros adicionales que se envían en la URL después del signo de interrogación (`?`). Se utilizan para enviar información adicional que no forma parte de la ruta.

#### Ejemplo con Query Params

```py
from flask import request

@app.route('/search')
def search():
    query = request.args.get('q')
    return f'Buscando: {query}'
```

En este ejemplo, el parámetro de búsqueda se envía en la URL de esta forma: `/search?q=flask`. El resultado será "Buscando: flask".
