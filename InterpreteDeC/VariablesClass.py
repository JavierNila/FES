class Variable:
    def __init__(self, nombre, tipo, valor=None):
        if nombre is not None and tipo is not None and valor is not None:
            self.nombre = nombre
            self.tipo = tipo
            self.valor = valor
        elif nombre is not None and tipo is None and valor is not None:
            self.nombre = nombre
            self.tipo = float(tipo)
            self.valor = valor
        else:
            self.nombre = nombre
            self.tipo = tipo
            self.valor = None