def crear_diccionario(texto):
    palabras = texto.lower().split()
    diccionario = palabras
    return diccionario

def guardar_diccionario(diccionario, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for palabra in diccionario:
            archivo.write(palabra + " ")

texto_usuario = input("Ingresa un texto: ")

diccionario_resultante = crear_diccionario(texto_usuario)

print("Diccionario Resultante: ")
for palabra in diccionario_resultante:
    print(palabra)

nombre_archivo = input("Ingresa el nombre del archivo txt para guardar el diccionario: ")
guardar_diccionario(diccionario_resultante, nombre_archivo + ".txt")