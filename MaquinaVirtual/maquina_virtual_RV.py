class Etiqueta:
    def __init__(self, nombre, linea):
        self.nombre = nombre
        self.linea = linea


def es_simbolo_esp(caracter):
    return caracter in "+-*;,.:!#=%&/(){}[]<><=>=="


def es_separador(caracter):
    return caracter in " \n\t"


def tokenizar(cadena):
    # Reemplaza las comas por un espacio seguido de una coma
    cadena = cadena.replace(',', ' ,')

    # Divide la cadena por espacios y devuelve la lista de tokens
    tokens = cadena.split()

    return tokens


instrucciones = []

arch = open('prog1.txt', 'r')
for ren in arch:
    if len(ren) > 2:
        datos = tokenizar(ren)
        instrucciones.append(datos)
arch.close()

pc = 0
registros = []
for c in range(32):
    registros.append(0)

# encontrar todas las etiquetas
etiquetas = []
for c in range(len(instrucciones)):
    if instrucciones[c][0] == '%':
        etiquetas.append(Etiqueta(instrucciones[c][1], c))


def get_dir_etiqueta(etq):
    direcion = -1
    for e in etiquetas:
        if e.nombre == etq:
            return e.linea
    return direccion


# imprimir todas las etiquetas
for e in etiquetas:
    print(e.nombre, e.linea)

while instrucciones[pc][0] != 'END':
    inst = instrucciones[pc]
    print(pc, registros[2], inst)
    if inst[0] == 'ADDI':
        destino = int(inst[1][1:])
        reg1 = int(inst[3][1:])
        numero = int(inst[5])
        registros[destino] = registros[reg1] + numero
        pc = pc + 1
    elif inst[0] == '%':
        pc = pc + 1
    elif inst[0] == 'J':  # Jump salta a la dirección indicada
        etq = inst[1]  # encontramos la etiqueta a donde saltar
        pc = get_dir_etiqueta(etq)  # buscamos la direccion en la tabla de etiquetas
        print('saltando a', pc)
    elif inst[0] == 'BGE':
        op1 = registros[int(inst[1][1:])]
        num = int(inst[3])
        etq = inst[5]
        print('comparando ', op1, 'con', num)
        if op1 >= num:
            pc = get_dir_etiqueta(etq)
        else:
            pc = pc + 1
