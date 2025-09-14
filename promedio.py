# -------------------------------------------------------
# Función: promedio_temperaturas
# Descripción: esta función recibe una lista de números
# (temperaturas) y devuelve el promedio de esas temperaturas.
# -------------------------------------------------------

def promedio_temperaturas(lista_temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.
    Parámetro:
        lista_temperaturas (list): Lista de números (int o float)
    Retorna:
        float: Promedio de los valores de la lista
    """
    return sum(lista_temperaturas) / len(lista_temperaturas)


# -------------------------------------------------------
# PRUEBAS DE LA FUNCIÓN
# -------------------------------------------------------

# Lista de temperaturas de Quito en una semana
temperaturas_quito = [22, 23, 21, 24, 20, 25, 23]
print("Promedio Quito:", promedio_temperaturas(temperaturas_quito))

# Lista de temperaturas de Guayaquil en una semana
temperaturas_guayaquil = [28, 29, 30, 27, 31, 32]
print("Promedio Guayaquil:", promedio_temperaturas(temperaturas_guayaquil))

# Lista de temperaturas de Cuenca en una semana
temperaturas_cuenca = [18, 19, 20, 21, 19, 18, 20]
print("Promedio Cuenca:", promedio_temperaturas(temperaturas_cuenca))