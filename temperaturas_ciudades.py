# Crear una matriz 3D que represente los datos de temperaturas diarias en varias ciudades. En una dimensión, puedes tener diferentes ciudades, en otra dimensión, días de la semana (Lunes, Martes, Miércoles, etc.), y en la tercera dimensión, semanas.

# Dentro de cada celda de la matriz, puedes almacenar las temperaturas diarias para una ciudad en un día específico de una semana determinada.

# Utilizar bucles anidados para calcular el promedio de temperaturas para una ciudad por cada una de las semanas.

# Mostrar el promedio de temperaturas para cada ciudad y semana en la pantalla.

# Ejemplo de datos
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4

# Matriz 3D: ciudades x semanas x días
import random
temperaturas = [
    [  # Para cada ciudad
        [random.randint(15, 35) for _ in dias_semana]  # Para cada semana, temperaturas diarias
        for _ in range(semanas)
    ]
    for _ in ciudades
]

# Calcular y mostrar promedios
for i, ciudad in enumerate(ciudades):
    print(f"Ciudad: {ciudad}")
    for j in range(semanas):
        suma = sum(temperaturas[i][j])
        promedio = suma / len(dias_semana)
        print(f"  Semana {j+1}: Promedio = {promedio:.2f}°C")
    print()

    