# Diccionarios - clave -> valor
diccionario = {
    'nombre': 'Renato',
    'apellidos': 'Condori Canaza',
    'especialidades': [
        {
            'nombre': 'Backend',
            'nivel': 'Sr'
        },
        {
            'nombre': 'Frontend',
            'nivel': 'Mid'
        }
    ]
}

print(f"Nombre: {diccionario['nombre']}")

especialidades = diccionario['especialidades']
print(f"Especialidades: {especialidades}")
print(f"1º Especialidad: {especialidades[0]['nombre']}")
print(f"Nivel 2º Especialidad: {especialidades[1]['nivel']}")
