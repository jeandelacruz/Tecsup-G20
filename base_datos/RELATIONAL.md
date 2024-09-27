# BASE DE DATOS RELACIONALES

### Componentes claves

- **Datos**: La información que almacenamos.
- **Tablas**: Es donde los datos se guardan organizadamente.
- **Motor de BD**: Programas que se usan para interactuar con una BD.
- **Indices**: Es parte de una estructura, y ayuda a mejorar la velocidad en las consultas.
- **KEY (Claves)**: Campos especificos que ayudan a identificar un registro (unico o compartido).

## Normalización

Nos ayuda a organizar los datos de forma eficiente, reduciendo la redundancia y evitando inconsistencias.

#### Primera Forma Normal (1NF)

1. Todos los atributos de una tabla contegan **valores atomicos**.
2. Cada entrada en una columna, debe ser de un valor y en toda fila sea unica.

`Antes de 1NF` (Incorrecto)

| cliente_id | nombre | telefono             |
| ---------- | ------ | -------------------- |
| 1          | Juan   | 123456789, 987688552 |
| 2          | Ana    | 555555555            |

El problema es que la columna **telefono**, tiene varios valores lo que rompe el principio de atomicidad.

`Despues de 1NF` (Correcto)

| cliente_id | nombre | telefono  |
| ---------- | ------ | --------- |
| 1          | Juan   | 123456789 |
| 1          | Juan   | 987688552 |
| 2          | Ana    | 555555555 |

Ahora cada celda tiene un solo valor, cumpliendo nuestra primera forma normal.

#### Segunda Forma Normal (2NF)

1. La base de datos ya este con la 1NF.
2. Todos los atributos no claves dependan completamente de una **clave primaria**.

`Antes de 2NF` (Incorrecto)

| venta_id | producto_id | nombre_producto | cliente_id | nombre_cliente |
| -------- | ----------- | --------------- | ---------- | -------------- |
| 1        | 101         | TV              | 100        | Juan           |
| 2        | 102         | Laptop          | 101        | Ana            |

**nombre_producto** depende solo de **producto_id**, y **nombre_cliente** depende solo de **cliente_id**.

`Despues de 2NF` (Correcto)

- Tabla de **ventas**

| venta_id | producto_id | cliente_id |
| -------- | ----------- | ---------- |
| 1        | 101         | 100        |
| 2        | 102         | 101        |

- Tabla de **productos**

| producto_id | nombre_producto |
| ----------- | --------------- |
| 101         | TV              |
| 102         | Laptop          |

- Tabla de **clientes**

| cliente_id | nombre_cliente |
| ---------- | -------------- |
| 100        | Juan           |
| 101        | Ana            |

Ahora, cada atributo depende completamente de la clave primaria en su respectiva tabla.

#### Tercera Forma Normal (3NF)

1. La base de datos ya debe estar en la 2NF.
2. No existen **dependencias transitivas**.

`Antes de 3NF` (Incorrecto)

| empleado_id | nombre_empleado | area_id | nombre_area | nombre_jefe |
| ----------- | --------------- | ------- | ----------- | ----------- |
| 1           | Pedro           | 10      | Ventas      | Juan        |
| 2           | Ana             | 20      | Marketing   | Laura       |

**nombre_area** depende de **area_id**, y **nombre_jefe** depende de **nombre_area**, aqui ya tenemos una dependencia transitiva, porque **nombre_jefe** depende indirectamente de **area_id** a traves de **nombre_area**.

`Despues de 3NF` (Correcto)

- Tabla de **empleados**

| empleado_id | nombre_empleado | area_id |
| ----------- | --------------- | ------- |
| 1           | Pedro           | 10      |
| 2           | Ana             | 20      |

- Tabla de **areas**

| area_id | nombre_area | nombre_jefe |
| ------- | ----------- | ----------- |
| 10      | Ventas      | Juan        |
| 20      | Marketing   | Laura       |

Ahora, **nombre_jefe** depende directamente de **area_id** en la tabla **areas**.

## Ejercicio

`Tabla sin normalizar`

| venta_id | cliente_nombre | cliente_email  | producto_nombre | cantidad | precio_unitario | vendedor_nombre | vendedor_telefono |
| -------- | -------------- | -------------- | --------------- | -------- | --------------- | --------------- | ----------------- |
| 1        | Juan           | juan@gmail.com | Televisor       | 1        | 500             | Pedro           | 985566888         |
| 2        | Juan           | juan@gmail.com | Lavadora        | 2        | 300             | Pedro           | 985566888         |
| 3        | Ana            | ana@gmail.com  | Televisor       | 1        | 500             | Laura           | 987123456         |

Aqui, tenemos redundancia en los datos.

- El **nombre** y el **email** del cliente se repiten para cada venta realizada.
- Los **datos** del vendedor tambien se repiten para cada venta.

Solucion:

- Ejecuten la 1NF (Ya se encuentra solucionada)

| venta_id | cliente_nombre | cliente_email  | producto_nombre | cantidad | precio_unitario | vendedor_nombre | vendedor_telefono |
| -------- | -------------- | -------------- | --------------- | -------- | --------------- | --------------- | ----------------- |
| 1        | Juan           | juan@gmail.com | Televisor       | 1        | 500             | Pedro           | 985566888         |
| 2        | Juan           | juan@gmail.com | Lavadora        | 2        | 300             | Pedro           | 985566888         |
| 3        | Ana            | ana@gmail.com  | Televisor       | 1        | 500             | Laura           | 987123456         |

- Ejecuten la 2NF

  - Tabla **ventas**

    | venta_id | cliente_id | producto_nombre | cantidad | precio_unitario | vendedor_id |
    | -------- | ---------- | --------------- | -------- | --------------- | ----------- |
    | 1        | 1          | Televisor       | 1        | 500             | 1           |
    | 2        | 1          | Lavadora        | 2        | 300             | 1           |
    | 3        | 2          | Televisor       | 1        | 500             | 2           |

  - Tabla **clientes**

    | cliente_id | cliente_nombre | cliente_email  |
    | ---------- | -------------- | -------------- |
    | 1          | Juan           | juan@gmail.com |
    | 2          | Ana            | ana@gmail.com  |

  - Tabla **vendedores**

    | vendedor_id | vendedor_nombre | vendedor_telefono |
    | ----------- | --------------- | ----------------- |
    | 1           | Pedro           | 985566888         |
    | 2           | Laura           | 987123456         |

- Ejecuten la 3NF

  - Tabla **ventas**

    | venta_id | cliente_id | producto_id | cantidad | vendedor_id |
    | -------- | ---------- | ----------- | -------- | ----------- |
    | 1        | 1          | 1           | 1        | 1           |
    | 2        | 1          | 2           | 2        | 1           |
    | 3        | 2          | 1           | 1        | 2           |

  - Tabla **clientes**

    | cliente_id | cliente_nombre | cliente_email  |
    | ---------- | -------------- | -------------- |
    | 1          | Juan           | juan@gmail.com |
    | 2          | Ana            | ana@gmail.com  |

  - Tabla **vendedores**

    | vendedor_id | vendedor_nombre | vendedor_telefono |
    | ----------- | --------------- | ----------------- |
    | 1           | Pedro           | 985566888         |
    | 2           | Laura           | 987123456         |

  - Tabla **productos**

    | product_id | producto_nombre | producto_precio_unitario |
    | ---------- | --------------- | ------------------------ |
    | 1          | Televisor       | 500                      |
    | 2          | Lavadora        | 300                      |
