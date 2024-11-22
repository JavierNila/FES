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
posJ='abcdefghijklmnopqrstuvwxyz'
posK='abcdefghijklmnopqrstuvwxyz'
posL='abcdefghijklmnopqrstuvwxyz'
posN='abcdefghijklmnopqrstuvwxyz'
posO='abcdefghijklmnopqrstuvwxyz'
posP='abcdefghijklmnopqrstuvwxyz'
posQ='abcdefghijklmnopqrstuvwxyz'
posR='abcdefghijklmnopqrstuvwxyz'
posS='abcdefghijklmnopqrstuvwxyz'
posT='abcdefghijklmnopqrstuvwxyz'
posU='abcdefghijklmnopqrstuvwxyz'
posV='abcdefghijklmnopqrstuvwxyz'
posW='abcdefghijklmnopqrstuvwxyz'
posX='abcdefghijklmnopqrstuvwxyz'
posY='abcdefghijklmnopqrstuvwxyz'
posZ='abcdefghijklmnopqrstuvwxyz'

c = 0
#prueba con ngvvwwx
for p in dic:
    if len(p) == 7:
        if p[2]==p[3] and p[4]==p[5]:
            if p[4] in posV and p[-1] in posX:
                if p[0] in posN and p[1] in posG:
                    c= c+1
                    #print(p)

#prueba con nsyqq
for p in dic:
    if len(p) == 5:
        if p[3]==p[-1]:
            if p[0] in posN and p[1] in posS and p[2] in posY:
                c=c+1
                #print(p)

#prueba con gsswi
for p in dic:
    if len(p)==5:
        if p[1]==p[2]:
            if p[-1] in posI and p[0] in posG and p[3] in posW:
                c=c+1
                #print(p)

#prueba con vakeais
for p in dic:
    if len(p)==7:
        if p[1]==p[4]:
            if p[-1] in posS and p[5] in posI:
                if p[0] in posV and p[2] in posK and p[3] in posE:
                    c=c+1
                    #print(p)

#prueba con xyttwi
for p in dic:
    if len(p)==6:
        if p[2]==p[3]:
            if p[-1] in posI and p[0] in posX:
                if p[1] in posY and p[4] in posW:
                    c=c+1
                    #print(p)

#prueba con aee
for p in dic:
    if len(p)==3:
        if p[1]==p[2]:
            if p[0] in posA:
                c=c+1
                #print(p)

#prueba con zw
for p in dic:
    if len(p)==2:
        if p[0] in posZ and p[1] in posW:
            c=c+1
            #print(p)

#prueba con pyk
for p in dic:
    if len(p)==3:
        if p[0] in posP and p[1] in posY and p[2] in posK:
            c=c+1
            #print(p)



alfabeto = 'abcdefghijklmnopqrstuvwxyz'
llave = 'lzvxwerpydbqktacjinsgXuhoX'
b=descifraSustituye('nsyqq ngtxlo leswitaatn dgns leswi xyttwi uwiw nlviwx sa pyk ltx pyn yxwl ae naqyx vakeais uln sa zw qwes yt gsswi naqysgxw eai sua ai spiww pagin. vatnwjgwtsqo, pw eyhwx pyn wow eyikqo gcat spw qlswns iwcaisn ae spw qwewziw-oanpyxl whcwxysyat sa klin (spyn atw uln sa slbw aee eiak qgtli zlnw ltx kyrps lvsglqqo ngvvwwx) ltx ciwswtxwx npw ulnt’s spwiw', llave)
print(b)
