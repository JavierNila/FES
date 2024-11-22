# Define funciones para determinar si un caracter es un símbolo especial, un separador, o un identificador.
def es_simbolo_esp(caracter):
    return caracter in "+-*;,.:!#=%&/(){}[]<><=>=\""


def es_simbolo_operacion(caracter):
    return caracter in "+-*/"


def es_separador(caracter):
    return caracter in " \n\t"


def es_id(cad):
    return cad[0] in "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


# Define funciones para determinar si una cadena es una palabra reservada o un tipo.
def es_palabra_reservada(cad):
    palres = ['print', 'read', 'tabla', 'var', 'println']
    return cad in palres


def es_tipo_datos(cad):
    tipos = ["int", "string", 'float', 'char']
    return cad in tipos
