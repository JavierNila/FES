from FES.InterpreteDeC.InterpreteCFor import *
from FES.InterpreteDeC.metodosPrint import metodo_print, metodo_println
from FES.InterpreteDeC.metodosTrigonometricos import calcular_trigonometrica
from VarMetodos import *
from ValorMetodos import *

tabla_var = []  # Inicializa la tabla de variables vacía
ren = ""  # Inicializa la variable 'ren' como una cadena vacía
while ren != 'end;':  # Loop mientras 'ren' no sea igual a 'end;'
    ren = input('$:')  # Solicita al usuario una entrada

    linea = quitar_comentarios(ren)

    tokens = separa_tokens(linea)  # Separa los tokens de la entrada

    if len(tokens) != 0:
        if es_palabra_reservada(tokens[0]):
            if tokens[-1] != ';':
                print('Falta el ";"')
                continue

            if es_tipo_datos(tokens[1]):
                if existe_var(tabla_var, tokens[2]):
                    agrega_var_valor(tabla_var, tokens[2], tokens[1])
                else:
                    print("Existe el valor en la tabla, ingresar otra variable")
                    continue
            elif tokens[0] == 'read':
                if tokens[1] == '(' and es_id(tokens[2]) and tokens[3] == ')':
                    leido = input(f'Escriba el valor de {tokens[2]}: ')  # Lee una entrada del usuario
                    set_var(tabla_var, tokens[2], leido)  # Asigna el valor leído a la variable en la tabla de variables
            elif tokens[0] == 'tabla':
                imprime_tabla_var(tabla_var)  # Imprime la tabla de variables
            elif tokens[0] == "print":
                metodo_print(tokens, tabla_var)
            elif tokens[0] == "println":
                metodo_println(tokens, tabla_var)
        # Realiza operaciones
        elif es_id(tokens[0]) and tokens[1] == "=":
            valores_variables = es_una_operacion(tabla_var, tokens)
            resultado = cambio_variable_dato(valores_variables, tokens[2:-1])
            agrega_var_valor(tabla_var, tokens[0], "float", resultado)
        # Loop for
        elif tokens[0] == "for":
            resultado = {'a': 1}
            variable, inicio, fin, cuerpo = convertir_loop_for(ren)
            resultado = ejecucion_loop_for(variable, inicio, fin, cuerpo, resultado)
            print(f"Resultado: a = {resultado['a']}")
        elif (tokens[0] == "sin" or tokens[0] == "cos" or tokens[0] == "tan") and tokens[-1] == ";":
            resultado = calcular_trigonometrica(tokens[0], int(tokens[2]))
            print(resultado)
        else:
            print("Formato invalido falta ';'")
    else:
        continue