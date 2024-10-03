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

## JOINS

Se utiliza para combinar filas de dos o más tablas en función de una condición relacionada entre ellas.

- Tabla **trabajadores**

| id  | nombre       | cargo                | area_id |
| --- | ------------ | -------------------- | ------- |
| 1   | Juan Perez   | Senior Desarrollador | 1       |
| 2   | Maria Gomez  | Gerente              | NULL    |
| 3   | Laura Torres | Tester               | 3       |

- Tabla **areas**

| id  | nombre           |
| --- | ---------------- |
| 1   | Tecnologia       |
| 2   | Marketing        |
| 3   | Recursos Humanos |
| 4   | Ventas           |

1. **INNER JOIN**: Devuelve las filas cuando **hay una coincidencia** en ambas tablas.

```sql
-- Listar todos los trabajadores con el nombre de su area
SELECT t.id, t.nombre, t.cargo, a.nombre AS area FROM trabajadores t
INNER JOIN areas a ON t.area_id = a.id;
```

2. **LEFT JOIN**: Devuelve todas las filas de la tabla izquierda, y las filas coincidentes de la tabla de la derecha.

```sql
-- Listar todos los trabajadores, incluso aquelos que no tienen una area asignada
SELECT t.id, t.nombre, t.cargo, a.nombre AS area FROM trabajadores t
LEFT JOIN areas a ON t.area_id = a.id ORDER BY t.id;
```

3. **RIGHT JOIN**: Similar a **LEFT JOIN**, pero este devuelve todos los datos de la tabla de la derecha y las coincidencias de la tabla izquierda.

```sql
-- Lista todos los areas, incluso si no tienen trabajadores asignados
SELECT t.id, t.nombre, t.cargo, a.nombre AS area FROM trabajadores t
RIGHT JOIN areas a ON t.area_id = a.id ORDER BY t.id;
```

4. **FULL OUTER JOIN**: Devuelve las filas cuando hay coincidencia en una de las tablas, si no hay coincidencia se completan con NULL.

```sql
-- Listas todas las filas de ambas tablas, incluso si no hay coincidencia
SELECT t.id, t.nombre, t.cargo, a.nombre AS area FROM trabajadores t
FULL OUTER JOIN areas a ON t.area_id = a.id ORDER BY t.id;
```
