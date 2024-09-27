# ¿Qué es una base de datos?

Es una `caja` donde guardamos información estructurada, como usuarios, productos, ventas o cualquier otro tipo de datos que podemos organizar o gestionar.

## Tipos de Base de datos

1. Bases de Datos Relacionales (SQL)

Almacena datos en `tablas` (una hoja de calculo). Cada tabla tiene **filas**, **columnas**, cada fila representa un registro y cada columna representa un campo (o atributo).

#### Ejemplos

- MySQL
- PostgreSQL
- SQLite

#### Ventajas

- Los datos estan organizados, de forma estructurada en tablas.
- Se pueden crear relaciones entre diferentes tablas.
- Aseguran la consistencia de los datos.

Una tabla de `usuarios`, que cuenta con las columnas `id, nombre, email`

| id  | nombre | email          |
| --- | ------ | -------------- |
| 1   | Juan   | juan@gmail.com |
| 2   | Ana    | ana@gmail.com  |

2. Bases de Datos No Relacionales

`NO UTILIZAN TABLAS PARA ORGANIZAR LOS DATOS.` Se almacena los datos de manera mas flexible, como **documentos** (formatos JSON o similar), **pares, claves-valor o colecciones de columnas (grafos)**. Son muy utilizadas cuando se requiere almacenar volumenes grandes de datos no estructurados o semi-estructuradas.

#### Ejemplos

- MongoDB
- Redis
- Cassandra

#### Ventajas

- Flexibilidad en la forma de almacenar datos.
- Escalabilidad, grandes volumenos datos para aplicaciones en tiempo real.
- Ideales para datos semi-estructurados o no estructurados.

`Documentos de usuarios, que no mantienen los mismos datos.`

```json
// 1er Documento
{
  "id": 1,
  "nombre": "Jossimar",
  "apellidos": "Chavez Romero",
  "direccion": {
    "calle": "Av. Principal 999",
    "ciudad": "Lima"
  }
}

// 2do Documento
{
    "id": 2,
    "nombre": "Kelvin",
    "apellidos": "Garcia"
}

// 3er Documento
{
    "id": 3,
    "nombre": "Miguel",
    "apellidos": "Torres",
    "edad": 28
}
```
