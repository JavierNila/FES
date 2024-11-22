from FES.InterpreteDeC.BooleanMetodos import es_id


def metodo_print(tokens, tabla_var):
    if tokens[1] == '(' and tokens[-2] == ')':

        if es_id(tokens[2]):
            for v in tabla_var:
                if v.nombre == tokens[2]:
                    print(str(v.valor) + str(tokens[4]), end="")
        elif es_id(tokens[4]):
            for v in tabla_var:
                if v.nombre == tokens[4]:
                    print(str(tokens[2]) + str(v.valor), end="")
        else:
            print(tokens[2], end="")


def metodo_println(tokens, tabla_var):
    if tokens[1] == '(' and tokens[-2] == ')':
        if es_id(tokens[2]):
            for v in tabla_var:
                if v.nombre == tokens[2]:
                    print(str(v.valor) + str(tokens[4]))
        elif es_id(tokens[4]):
            for v in tabla_var:
                if v.nombre == tokens[4]:
                    print(str(tokens[2]) + str(v.valor))
        else:
            print(str(tokens[2]))
