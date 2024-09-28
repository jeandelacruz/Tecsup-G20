# DML - Lenguaje de Manipulación de Datos

Comandos, que permiten gestionar y/o manipular datos en una base de datos.

Los comandos mas comunes:

- `INSERT`: para insertar datos en una tabla.
- `UPDATE`: para modificar datos existentes en una tabla.
- `DELETE`: para eliminar datos de una tabla.
- `SELECT`: para consultar y/o recuperar datos de una tabla.

### Ejemplos

1. Insertar un dato en una tabla

```sql
INSERT INTO nombre_tabla (columna) VALUES (valor_columna);
```

2. Insertar varios filas en una tabla

```sql
INSERT INTO nombre_tabla (columna)
VALUES
(valor_columna_1),
(valor_columna_2),
(valor_columna_3);
```

3. Consulta de datos de una tabla

```sql
-- Traemos todos los datos incluyendo todas las columnas de una tabla
SELECT * FROM nombre_tabla;
```

```sql
-- Si deseamos traer solo algunas columnas
SELECT nombre_columna FROM nombre_tabla;
```

4. Actualizar datos de una tabla

```sql
UPDATE nombre_tabla SET nombre_columna = 'valor_columna' WHERE nombre_columna = 'valor_filtro';
```

5. Eliminar datos de una tabla

```sql
-- Eliminar todos los registros de mi tabla
DELETE FROM nombre_tabla;
```

```sql
DELETE FROM nombre_tabla WHERE nombre_columna = 'valor_columna';
```
