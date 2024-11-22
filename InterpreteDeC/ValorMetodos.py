def convertir_valor(valor, tipo_dato):
    try:
        if tipo_dato == "int":
            return int(valor)
        elif tipo_dato == "float":
            return float(valor)
        elif tipo_dato == "str":
            return str(valor)
        elif tipo_dato == "char":
            return chr(valor)
        else:
            return valor
    except ValueError:
        return valor  # Si hay un error al convertir, mantener el valor como está


def buscar_variable(tabla, variable):
    for v in tabla:
        if v.nombre == variable and v.valor != None:
            print("Existe el valor y la variable")
    return None


def es_una_operacion(tabla_variables, lista_tokens):
    valores_variables = []
    for variable in tabla_variables:
        if variable.nombre in lista_tokens:
            if variable.valor != None and type(variable.valor) != list:
                variable_dato = (variable.nombre, variable.valor)
                valores_variables.append(variable_dato)
            else:
                continue
    if len(valores_variables) >= 2:
        return valores_variables


def cambio_variable_dato(valores, expresion):
    expresion_str = " ".join(expresion)
    for variable, valor in valores:
        expresion_str = expresion_str.replace(variable, str(valor))
    return eval(expresion_str)