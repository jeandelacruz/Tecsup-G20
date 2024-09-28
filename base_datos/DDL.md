# DDL - Lenguaje de Definicion de Datos

Comandos, que permiten definir y gestionar la estructura de una base de datos.

- Creación
- Modificación
- Eliminación

Objetos como bases de datos, tablas, indices, etc.

Los comandos más comunes:

- `CREATE`: para crear base de datos, tablas, indices, etc.
- `ALTER`: para modificar estructuras existentes.
- `DROP`: para eliminar objetos.
- `RENAME`: para cambiar el nombre de un objeto.

### Ejemplos

1. Crear una base de datos

```sql
-- mi_base_datos, pueden elegir cualquier nombre.
CREATE DATABASE mi_base_datos;
```

2. Eliminar una base de datos

```sql
-- mi_base_datos, pueden elegir cualquier nombre.
DROP DATABASE mi_base_datos;
```

3. Renombrar una base de datos

```sql
-- nueva_base_datos, pueden elegir cualquier nombre.
ALTER DATABASE mi_base_datos RENAME TO nueva_base_datos;
```

4. Crear una tabla con un campo autoincrementable

```sql
CREATE TABLE nombre_tabla (
    -- Se detalla los campos o columnas
    -- https://www.ibiblio.org/pub/Linux/docs/LuCaS/Tutoriales/NOTAS-CURSO-BBDD/notas-curso-BD/node134.html
    -- nombre_campo tipo_dato opciones
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);
```
