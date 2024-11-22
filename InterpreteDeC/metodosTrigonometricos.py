import math


def calcular_trigonometrica(funcion, angulo):
    angulo_radianes = math.radians(angulo)
    resultado = getattr(math, funcion)(angulo_radianes)
    return resultado
