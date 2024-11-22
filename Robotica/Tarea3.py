import math


# Función para convertir grados a radianes
def grados_a_radianes(angulo):
    return angulo * math.pi / 180


# Función para calcular la posición del efector final
def calcular_posicion(theta1, theta2, L1=20, L2=20, c=5):
    # Convertir los ángulos a radianes
    theta1 = grados_a_radianes(theta1)
    theta2 = grados_a_radianes(theta2)

    # Cinemática directa para el robot de 2 GDL
    x = L1 * math.cos(theta1) + L2 * math.cos(theta1 + theta2) + c
    y = L1 * math.sin(theta1) + L2 * math.sin(theta1 + theta2)

    return x, y


# Solicitar al usuario los ángulos theta1 y theta2
def main():
    print("Cinemática Directa de un Robot de 2 GDL")
    theta1 = float(input("Introduce un valor para theta1: "))
    theta2 = float(input("Introduce un valor para theta2: "))

    # Calcular la posición del efector final
    x, y = calcular_posicion(theta1, theta2)

    # Mostrar el resultado
    print(f"La posición del efector final es: xd = {x:.2f} cm, yd = {y:.2f} cm")

    input("Presionar enter para finalizar el programa")


if __name__ == "__main__":
    main()
