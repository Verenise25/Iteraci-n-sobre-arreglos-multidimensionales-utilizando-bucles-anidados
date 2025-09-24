# crear el diccionario personal
informacion_personal = {
    "nombre": "Melany",
    "edad": 28,
    "ciudad": "Guayas",
    "profesion": "Abogada"
}

# acceder y modificar valores
print("Ciudad:", informacion_personal["ciudad"])
informacion_personal["ciudad"] = "Quito"
print("Ciudad actualizada:", informacion_personal["ciudad"])

# agregar nueva clave-valor "profesion"
informacion_personal["profesion"] = "Estudiante"
print("Profesión:", informacion_personal["profesion"])

# verificar existencia de la clave "telefono"
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0985852361"

# eliminar la clave "edad"
del informacion_personal["edad"] 

# imprimir el diccionario actualizado
print("Diccionario actualizado:", informacion_personal)
