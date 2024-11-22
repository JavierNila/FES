import re

from FES.InterpreteDeC.BooleanMetodos import *
from FES.InterpreteDeC.ValorMetodos import convertir_valor
from FES.InterpreteDeC.VariablesClass import Variable


def agrega_var(tabla_var, nombre, tipo):
    tabla_var.append(Variable(nombre, tipo))


def agrega_var_valor(tabla_var, nombre, tipo, valor=None):
    tabla_var.append(Variable(nombre, tipo, valor))


# Define una función para verificar si una variable existe en la tabla de variables.
def existe_var(tabla_var, nombre):
    encontrado = False

    list_nombre = []
    for i in tabla_var:
        list_nombre.append(i.nombre)

    if len(tabla_var) != 0:
        for v in tabla_var:
            if v.nombre != nombre and list_nombre.count(nombre) < 1:
                encontrado = True
    else:
        encontrado = True
    return encontrado


# Define una función para asignar un valor a una variable en la tabla de variables.
def set_var(tabla_var, nombre, valor):
    count_var = []
    for i in tabla_var:
        count_var.append(i.nombre)

    if nombre in count_var:
        for v in tabla_var:
            if v.nombre == nombre and v.valor is None:
                tipo_dato = v.tipo
                valor = convertir_valor(valor, tipo_dato)
                v.valor = valor
                break
            else:
                continue
    else:
        print('variable ', nombre, 'no encontrada')
        return None


# Define una función para imprimir la tabla de variables.
def imprime_tabla_var(tabla_var):
    print()
    print('   Tabla de variables')
    print('nombre\t\ttipo\t\tvalor')
    for v in tabla_var:
        print(v.nombre, '\t\t', v.tipo, '\t\t', v.valor)
    return None


# Define una función para separar tokens en una línea de código.
def separa_tokens(linea):
    if len(linea) < 3:
        return []
    else:
        tokens = []
        tokens2 = []
        dentro = False
        try:
            for l in linea:
                if es_simbolo_esp(l) and not (dentro):
                    tokens.append(l)
                if (es_simbolo_esp(l) or es_separador(l)) and dentro:
                    tokens.append(cad)
                    dentro = False
                    if es_simbolo_esp(l):
                        tokens.append(l)
                if not (es_simbolo_esp(l)) and not (es_separador(l)) and not (dentro):
                    dentro = True
                    cad = ""
                if not (es_simbolo_esp(l)) and not (es_separador(l)) and dentro:
                    cad = cad + l
            compuesto = False
            for c in range(len(tokens) - 1):
                if compuesto:
                    compuesto = False
                    continue
                if tokens[c] in "=<>!" and tokens[c + 1] == "=":
                    tokens2.append(tokens[c] + "=")
                    compuesto = True
                else:
                    tokens2.append(tokens[c])
            tokens2.append(tokens[-1])
            for c in range(1, len(tokens2) - 1):
                if tokens2[c] == "." and es_tipo_datos(tokens2[c - 1]) and es_tipo_datos(tokens2[c + 1]):
                    tokens2[c] = tokens2[c - 1] + tokens2[c] + tokens2[c + 1]
                    tokens2[c - 1] = "borrar"
                    tokens2[c + 1] = "borrar"
            porBorrar = tokens2.count("borrar")
            for c in range(porBorrar):
                tokens2.remove("borrar")
            tokens = []
            dentroCad = False
            cadena = ""
            for t in tokens2:
                if dentroCad:
                    if t[-1] == '"':
                        cadena = cadena + " " + t
                        tokens.append(cadena[1:-1])
                        dentroCad = False
                    else:
                        cadena = cadena + " " + t
                elif ((t[0] == '"')):
                    cadena = t;
                    dentroCad = True
                else:
                    tokens.append(t)

            return tokens

        except Exception as e:
            print('Error, no se encuentra el ";" , favor de ingresar de nuevo')
            return []


def tiene_puntocoma(list_tokens):
    if list_tokens[-1] == ";":
        return True
    else:
        return False


def quitar_comentarios(linea):
    # Utilizamos una expresión regular para encontrar y reemplazar los comentarios
    linea_sin_comentarios = re.sub(r'/\*.*?\*/', '', linea)
    return linea_sin_comentarios.strip()