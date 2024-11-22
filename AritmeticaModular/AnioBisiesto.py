def anio_bisiesto(anio):
        if anio % 4 == 0:
            if anio % 100 == 0:
                if anio % 400 == 0:
                    return "es un año bisiesto aun si es divisible entre 100 lo es entre 400"
                else:
                    return "no es un año bisiesto porque es divisible entre 100"
            return "es un año bisiesto"
        else:
            return "no es año bisiesto"

anio = int(input("Año a calcular: "))
print(anio_bisiesto(anio))