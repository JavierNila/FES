import math
import random
from FES.ModeladoSimulacion.PrimerTarea import pov


def getXMax(v, ang):
    return (v ** 2) * math.sin(ang) / 9.8


def getYMax(v, ang):
    vy = v * math.sin(ang)
    t = vy / 9.8
    return (vy * t - 0.5 * 9.8 * t ** 2)


def tiroPara(v, angulo, t):
    vx = v * math.cos(angulo)
    vy = v * math.sin(angulo)
    x = vx * t
    y = vy * t - 0.5 * 9.8 * t ** 2
    return [x, y]


def blobEsfera(x, y, z, r, fuerza):
    texto = f" sphere{{<{x}, {y}, {z}>, {r}, {fuerza}}}\n"
    return texto


v = 50
angulo = 55
angulo = math.radians(angulo)
xmax = getXMax(v, angulo)

salida = open("salida.pov", "w")

cad = pov.povBasico()
cad += pov.povCamara(0, 30, xmax * 2, 0, 30, 0)
cad += pov.povLuz(1000, 1000, 1000, 1, 1, 1)
cad += pov.povPiso()
cad += pov.povTextura(1)
cad += pov.povTextura(2)
cad += pov.povTextura(3)
cad += pov.povTextura(4)
cad += "blob{\n threshold 0.6\n"

nTiros = 14
for c in range(nTiros):  # La cantidad de tiros parabólicos distintos
    aleV = random.randint(0, v // 8)  # La velocidad varía hasta en un décimo
    aleAngulo = random.random() / 4.2  # El ángulo puede variar hasta 1/4 de radian
    for t in range(30):
        ale = random.random()
        pos = tiroPara(v + aleV, angulo + aleAngulo, t / 5.2)
        angRot = math.radians(360 / (c + 1))  # Ángulo de rotación
        x = pos[0] * math.cos(angRot)
        z = pos[0] * math.sin(angRot)
        y = pos[1]
        cad += blobEsfera(x, y, z, 2.7 + ale, 1.0)
    salida.write(cad)
    cad = ""

cad = "texture{t2}}\n"
salida.write(cad)
salida.close()















