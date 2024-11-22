import re


def convertir_loop_for(for_loop):
    # Patrón para for del tipo: for (c = inicio; fin) { código }
    pattern = r'for\s*\(\s*([a-zA-Z_]\w*)\s*=\s*([^;]+)\s*;\s*([^;]+)\s*\)\s*\{([^}]*)\}'
    match = re.match(pattern, for_loop.strip())
    if match:
        variable = match.group(1).strip()
        inicio = match.group(2).strip()
        fin = match.group(3).strip()
        cuerpo = match.group(4).strip()
        return variable, inicio, fin, cuerpo
    else:
        raise ValueError("Formato del 'for' no válido")


def traducir_c_a_python(c_decl):
    # Traduce 'c = inicio' directamente sin cambiar nada
    return c_decl


def ejecucion_loop_for(variable, inicio, fin, cuerpo, local_context=None):
    if local_context is None:
        local_context = {}

    # Traducir la declaración de C a Python
    inicio_python = traducir_c_a_python(inicio)

    # Ejecutar el inicio para inicializar las variables
    exec(f'{variable} = {inicio_python}', {}, local_context)

    # Convertir fin a un entero en el contexto local
    fin_valor = eval(fin, {}, local_context)

    # Crear una función para evaluar la condición en el contexto local
    def eval_condicion():
        return local_context[variable] < fin_valor

    # Crear una función para ejecutar el incremento en el contexto local
    def exec_incremento():
        local_context[variable] += 1

    # Ejecutar el cuerpo del bucle en el contexto local
    while eval_condicion():
        exec(cuerpo, {}, local_context)
        exec_incremento()

    return local_context

