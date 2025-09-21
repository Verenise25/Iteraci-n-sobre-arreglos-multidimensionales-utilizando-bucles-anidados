# -------------------------------------------------------
# Función: calcular_descuento
# Descripción:
#   Esta función recibe el monto total de la compra y un
#   porcentaje de descuento (por defecto 10%).
#   Calcula el valor del descuento y lo devuelve.
# -------------------------------------------------------

def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento de una compra.
    Parámetros:
        monto_total (float): El total de la compra.
        porcentaje_descuento (float): El porcentaje a descontar (por defecto 10%).
    Retorna:
        float: El valor del descuento aplicado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# -------------------------------------------------------
# PROGRAMA PRINCIPAL (pruebas de la función)
# -------------------------------------------------------

# Caso 1: usando el valor por defecto (10%)
monto1 = 100.0
descuento1 = calcular_descuento(monto1)
total1 = monto1 - descuento1
print(f"Compra: ${monto1} | Descuento: ${descuento1} | Total a pagar: ${total1}")

# Caso 2: usando un valor de descuento específico (20%)
monto2 = 250.0
descuento2 = calcular_descuento(monto2, 20)
total2 = monto2 - descuento2
print(f"Compra: ${monto2} | Descuento: ${descuento2} | Total a pagar: ${total2}")

