import matplotlib.pyplot as plt
import numpy as np

# Datos actualizados (incluyendo los nuevos datos)
generaciones = [
    1, 2, 6, 22, 25, 42, 62, 74, 77, 80, 88, 90, 93, 94, 121, 132, 149,
    163, 177, 188, 194, 201, 213, 222, 244, 338, 363, 376, 397, 401, 405, 413, 418, 434, 482, 491, 496
]
porcentajes = [
    7.33, 7.67, 8.0, 9.67, 10.33, 12.33, 13.33, 13.5, 13.67, 14.0, 14.33, 14.5, 15.0, 15.33, 16.0, 16.67, 17.5,
    17.833333333333332, 18.0, 19.0, 19.166666666666668, 19.166666666666668, 19.666666666666668,
    19.833333333333332, 20.0, 20.166666666666668, 20.5, 22.166666666666668, 22.333333333333332,
    22.333333333333332, 22.5, 23.166666666666668, 23.333333333333332, 23.5, 23.833333333333332, 24.0, 24.166666666666668
]

# Extender las generaciones hasta la última para suavizar la curva
generaciones_completas = np.arange(1, 496 + 1)  # Ajusta el límite superior al último valor de generaciones
porcentajes_suavizados = np.interp(
    generaciones_completas, generaciones, porcentajes
)

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(
    generaciones_completas, porcentajes_suavizados, color="b", label="Progreso de reconocimiento"
)
plt.scatter(generaciones, porcentajes, color="red", label="Datos originales")  # Puntos originales

# Personalización de la gráfica
plt.title("Porcentaje de Reconocimiento vs Generaciones", fontsize=16)
plt.xlabel("Generaciones", fontsize=14)
plt.ylabel("Porcentaje de Reconocimiento (%)", fontsize=14)
plt.grid(True, linestyle="--", alpha=0.7)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=12)

# Mostrar la gráfica
plt.show()