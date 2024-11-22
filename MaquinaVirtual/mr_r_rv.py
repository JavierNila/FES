import tkinter as tk
from tkinter import filedialog

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


class Interfaz:
    def __init__(self, master):
        self.master = master
        self.master.title("Interprete de Ensamblador RISC-V")

        # Botón para cargar el programa
        self.boton_cargar = tk.Button(master, text="Cargar Programa", command=self.cargar_programa)
        self.boton_cargar.pack()

        # Botón para correr el programa
        self.boton_correr = tk.Button(master, text="Correr Programa", command=self.correr_programa)
        self.boton_correr.pack()

        # Botón para ejecutar paso a paso
        self.boton_paso_a_paso = tk.Button(master, text="Ejecutar Paso a Paso", command=self.ejecutar_paso_a_paso)
        self.boton_paso_a_paso.pack()

        # Contador de programa
        self.contador_programa = tk.Label(master, text="Contador de Programa: 0")
        self.contador_programa.pack()

        # Registros
        self.valores_registros = [0 for _ in range(32)]
        self.registros = [tk.Label(master, text=f"Registro {i}: {self.valores_registros[i]}") for i in range(32)]
        for registro in self.registros:
            registro.pack()

    def cargar_programa(self):
        filename = filedialog.askopenfilename()
        print(f'Programa cargado: {filename}')
        arch = open(filename, 'r')
        for ren in arch:
            if len(ren)>2:
                datos = tokenizar(ren)
                instrucciones.append(datos)
        arch.close()
        self.etiquetas = []
        for c in range(len(instrucciones)):
            if instrucciones[c][0] == '%':
                self.etiquetas.append(Etiqueta(instrucciones[c][1], c))

    def get_dir_etiqueta(self, etq):
        direcion = -1
        for e in self.etiquetas:
            if e.nombre == etq:
                return e.linea
        return direccion

    def correr_programa(self):
        pc = 0
        print('Corriendo programa...')
        while instrucciones[pc][0]!='END':
            inst = instrucciones[pc]
            print(pc, self.valores_registros[2], inst)
            if inst[0]=='ADDI':
                destino = int(inst[1][1:])
                reg1 = int(inst[3][1:])
                numero = int(inst[5])
                self.valores_registros[destino] = self.valores_registros[reg1] + numero
                pc = pc + 1
            elif inst[0]=='SUBI': #AGREGANDO RESTA
                destino = int(inst[1][1:])
                reg1 = int(inst[3][1:])
                numero = int(inst[5])
                pc = pc + 1
                self.valores_registros[destino] = self.valores_registros[reg1] - numero
            elif inst[0] == 'MULI':  #AGREGANDO MULTIPLICACION
                destino = int(inst[1][1:])
                reg1 = int(inst[3][1:])
                numero = int(inst[5])
                self.valores_registros[destino] = self.valores_registros[reg1] * numero
                pc = pc + 1
            elif inst[0] == '%':
                pc = pc + 1
            elif inst[0] == 'J': #Jump salta a la dirección indicada
                etq = inst[1]    # encontramos la etiqueta a donde saltar
                pc = self.get_dir_etiqueta(etq)  #buscamos la direccion en la tabla de etiquetas
                print('saltando a', pc)
            elif inst[0] == 'BGE':
                op1 = self.valores_registros[int(inst[1][1:])]
                num = int(inst[3])
                etq = inst[5]
                print('comparando ' , op1, 'con', num)
                if op1 >= num:
                    pc = self.get_dir_etiqueta(etq)
                else:
                    pc = pc + 1
            self.actualizar_registros()

    def ejecutar_paso_a_paso(self):
        print('Ejecutando paso a paso...')
        # Aquí puedes agregar el código para ejecutar tu programa paso a paso
        self.actualizar_registros()

    def actualizar_registros(self):
        for i in range(32):
            self.registros[i].config(text=f"Registro {i}: {self.valores_registros[i]}")



root = tk.Tk()
app = Interfaz(root)
root.mainloop()