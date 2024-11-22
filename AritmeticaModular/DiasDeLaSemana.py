dias=["domingo", "lunes", "martes", "miercoles", "jueves", "viernes", "sabado"]
def imprime_dias():
    for dia in dias:
        print(dia + ": " + str(dias.index(dia)))

def calcula_dia(dia, dia_calculo):
    calcula_dia = dia + dia_calculo
    return dias[calcula_dia]

imprime_dias()
num_dia = int(input("Valor de un dia: "))
dia_calculo = int(input("Dia a calcular: "))
print(calcula_dia(num_dia,dia_calculo))

