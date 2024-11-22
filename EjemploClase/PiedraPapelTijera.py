import random


def get_ganador(usuario, compu):
    if (usuario == 0 and compu == 2) or (usuario == 1 and compu == 0) or (usuario == 2 and compu == 1):
        return ('usuario')
    else:
        return ('compu')
    return ('empate')


opciones = {0: 'piedra', 1: 'papel', 2: 'tijeras'}
# el usuario da su opción
print('0:piedra')
print('1:papel')
print('2:tijeras')
usuario = int(input('escriba su opción:'))
# la computadora escoje
compu = random.choice([0, 1, 2])

print('usted seleccionó: ', opciones[usuario])
print('la compu seleccionó: ', opciones[compu])
gana = get_ganador(usuario, compu)
print('y el ganador es:', gana)