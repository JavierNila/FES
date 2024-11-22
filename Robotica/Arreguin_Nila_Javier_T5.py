import numpy as np

# Parámetros
tiempo_inicial = 0  # Tiempo inicial en segundos
tiempo_final = 50   # Tiempo final en segundos
muestreo = 0.001    # Tiempo de muestreo en segundos

# Generación del arreglo de tiempo
tiempo = np.arange(tiempo_inicial, tiempo_final + muestreo, muestreo)

# Guardar el arreglo en un archivo .txt
np.savetxt('arreglo_tiempo.txt', tiempo, fmt='%.3f', header="Arreglo de tiempo de 0 a 50 segundos con un muestreo de 0.001 s")

print("Archivo generado exitosamente.")
