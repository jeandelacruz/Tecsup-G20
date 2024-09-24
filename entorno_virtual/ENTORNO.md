# Entornos virtuales

1º Crear el entorno

```py
python -m venv nombre_entorno
```

2º Activar el entorno

```py
source nombre_entorno/Scripts/activate
```

3º Desactivar el entorno

```py
deactivate
```

# Gestionar librerias externas

- Listar librerias instaladas

```py
pip list
```

- Instalar librerias

```py
pip install nombre_libreria

-- Version
pip install nombre_libreria==1.00
```

- Guardar librerias instaladas (requirements.txt)

```py
pip freeze > requirements.txt
```

- Instalar todo lo del requirements.txt

```py
pip install -r requirements.txt
```

- Desinstalar librerias

```py
pip uninstall nombre_libreria
```
