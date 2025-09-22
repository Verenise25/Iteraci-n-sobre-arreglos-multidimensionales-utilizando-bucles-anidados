# crear el diccionario personal
mi_diccionario = {
    "nombre": "Melany",
    "edad": 28,
    "ciudad": "Guayas",
    "profesion": "Abogada"
}

# acceder y mostrar la ciudad
print("Ciudad:", mi_diccionario["ciudad"])

# modificar la edad
mi_diccionario["edad"] = 29

# verificar existencia de la clave "telefono"
if "telefono" not in mi_diccionario:
    mi_diccionario["telefono"] = "0985852361"

# eliminar la clave "edad"
del mi_diccionario["edad"] 

# imprimir el diccionario actualizado
print("Diccionario actualizado:", mi_diccionario)
