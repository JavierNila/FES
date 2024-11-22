import random

def cargaPalabras():
    archivo = open('words.txt', 'r')
    renglon = archivo.readline()
    palabras = renglon.split()
    print (len(palabras), 'palabras leidas')
    return palabras

def cargaCifrado():
    archivo = open('cifrado.txt', 'r')
    renglon = archivo.readline()
    return renglon

def descifraSustituye(cadena, alfabetoLlave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    nuevaCadena = ""
    for letra in cadena:
        if letra in alfabeto:
            posicion = alfabetoLlave.find(letra)
            nuevaCadena = nuevaCadena + alfabeto[posicion]
        else:
            nuevaCadena = nuevaCadena + letra
    return nuevaCadena


dic = cargaPalabras()
cifrado = cargaCifrado()

posA='abcdefghijklmnopqrstuvwxyz'
posB='abcdefghijklmnopqrstuvwxyz'
posC='abcdefghijklmnopqrstuvwxyz'
posD='abcdefghijklmnopqrstuvwxyz'
posE='abcdefghijklmnopqrstuvwxyz'
posG='abcdefghijklmnopqrstuvwxyz'
posH='abcdefghijklmnopqrstuvwxyz'
posI='abcdefghijklmnopqrstuvwxyz'
posK='abcdefghijklmnopqrstuvwxyz'
posL='abcdefghijklmnopqrstuvwxyz'
posO='abcdefghijklmnopqrstuvwxyz'
posP='abcdefghijklmnopqrstuvwxyz'
posQ='abcdefghijklmnopqrstuvwxyz'
posR='abcdefghijklmnopqrstuvwxyz'
posS='abcdefghijklmnopqrstuvwxyz'
posT='abcdefghijklmnopqrstuvwxyz'
posU='abcdefghijklmnopqrstuvwxyz'
posV='abcdefghijklmnopqrstuvwxyz'
posX='abcdefghijklmnopqrstuvwxyz'
posY='abcdefghijklmnopqrstuvwxyz'
posZ='abcdefghijklmnopqrstuvwxyz'

c = 0

##probando con qogdzogd.
'''for p in dic:
    if len(p)==8:
        if p[1]==p[5] and p[3]==p[-1] and p[2]==p[6]:
            if p[0]== 'd' and p[1] in posO and p[-1] in posD:
                    c = c + 1
                    print(p)'''
# probando con gvvxvdq
'''for p in dic:
    if len(p)==7:
        if p[0] in posG and p[1] in posV:
            if p[1]==p[2] and p[2]== p[4]:
                if p[-1] in posQ and p[-2] in posD:
                    c = c + 1
                    print(p)'''



#alfabeto='abcdefghijklmnopqrstuvwxyz'
#llave  = 'rhkqvsyplXxbidoaXeuzcXgXtX'
#b=descifraSustituye('l prq r yevrz gvvxvdq. od selqrt rszvedood, l sldlupvq goex rz 5 ai. l gvdz poiv rdq zoox r upogve. zpvd l gvdz zo uvv r kocabv os it selvdqu rz r hre qogdzogd.', llave)
#print(b)
