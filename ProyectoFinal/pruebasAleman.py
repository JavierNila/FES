def cargaPalabras():
    archivo = open('Aleman.txt', 'r')
    renglon = archivo.readline()
    palabras = renglon.split()
    print (len(palabras), 'palabras leidas')
    return palabras

def descifraSustituye(cadena, alfabetoLlave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyzäöüß'
    nuevaCadena = ""
    for letra in cadena:
        if letra in alfabeto:
            posicion = alfabetoLlave.find(letra)
            nuevaCadena = nuevaCadena + alfabeto[posicion]
        else:
            nuevaCadena = nuevaCadena + letra
    return nuevaCadena

dic = cargaPalabras()

posA='abcdefghijklmnopqrstuvwxyzäöüß'
posC='abcdefghijklmnopqrstuvwxyzäöüß'
posD='abcdefghijklmnopqrstuvwxyzäöüß'
posE='abcdefghijklmnopqrstuvwxyzäöüß'
posF='abcdefghijklmnopqrstuvwxyzäöüß'
posG='abcdefghijklmnopqrstuvwxyzäöüß'
posI='abcdefghijklmnopqrstuvwxyzäöüß'
posJ='abcdefghijklmnopqrstuvwxyzäöüß'
posK='abcdefghijklmnopqrstuvwxyzäöüß'
posL='abcdefghijklmnopqrstuvwxyzäöüß'
posM='abcdefghijklmnopqrstuvwxyzäöüß'
posO='abcdefghijklmnopqrstuvwxyzäöüß'
posP='abcdefghijklmnopqrstuvwxyzäöüß'
posQ='abcdefghijklmnopqrstuvwxyzäöüß'
posR='abcdefghijklmnopqrstuvwxyzäöüß'
posS='abcdefghijklmnopqrstuvwxyzäöüß'
posT='abcdefghijklmnopqrstuvwxyzäöüß'
posU='abcdefghijklmnopqrstuvwxyzäöüß'
posV='abcdefghijklmnopqrstuvwxyzäöüß'
posX='abcdefghijklmnopqrstuvwxyzäöüß'
posY='abcdefghijklmnopqrstuvwxyzäöüß'
posZ='abcdefghijklmnopqrstuvwxyzäöüß'
posÜ='abcdefghijklmnopqrstuvwxyzäöüß'
c = 0
print("------------teiez-----------")
#prueba con Teiez
for p in dic:
    if len(p)==5:
        if p[1]==p[3]:
            if p[0] in posT and p[2] in posI and p[-1] in posZ:
                c=c+1
                print(p)
print("--------------cmete------------------")
#prueba con cmete
for p in dic:
    if len(p)==5:
        if p[2]==p[-1]:
            if p[0] in posC and p[1] in posM and p[3] in posT:
                c=c+1
                print(p)
print("----------------sdp-----------------")
#prueba con sdp
for p in dic:
    if len(p)==3:
        if p[0] in posS and p[1] in posD and p[2] in posP:
            c=c+1
            print(p)
print("--------------cay-------------------")
#prueba con cay
for p in dic:
    if len(p)==3:
        if p[0] in posC and p[1] in posA and p[2] in posY:
            c=c+1
            print(p)
print("--------------puzy-------------------")
#prueba con Puzy
for p in dic:
    if len(p)==4:
        if p[0] in posP and p[1] in posU:
            if p[2] in posZ and p[3] in posZ:
                c=c+1
                print(p)
print("-----------------pez------------------")
#prueba con pez
for p in dic:
    if len(p)==3:
        if p[0] in posP and p[1] in posE and p[2] in posZ:
            c=c+1
            print(p)
print("--------------omvrv------------------")
#prueba con omvrv
for p in dic:
    if len(p)==5:
        if p[2]==p[-1]:
            if p[0] in posO and p[1] in posM and p[3] in posR:
                c=c+1
                print(p)
print("----------------Zmjjed---------------")
#prueba con Zmjjed
for p in dic:
    if len(p)==6:
        if p[2]==p[3]:
            if p[0] in posZ and p[1] in posM:
                if p[4] in posE and p[5] in posD:
                    c=c+1
                    print(p)
print("------------------kezr--------------")
#prueba con Kezr
for p in dic:
    if len(p)==4:
        if p[0] in posK and p[1] in posE:
            if p[2] in posZ and p[3] in posR:
                c=c+1
                print(p)
print("--------------kmez------------------")
#prueba con Kmez
for p in dic:
    if len(p)==4:
        if p[0] in posK and p[1] in posM:
            if p[2] in posE and p[3] in posZ:
                c=c+1
                print(p)
print("-------------usg--------------------")
#prueba con usg
for p in dic:
    if len(p)==3:
        if p[0] in posU and p[1] in posS and p[2] in posG:
            c=c+1
            print(p)
print("-----------------Tsdxe--------------------")
#prueba de Tsdxe
for p in dic:
    if len(p)==5:
        if p[0] in posT and p[1] in posS and p[2] in posD:
            if p[3] in posX and p[4] in posE:
                c=c+1
                print(p)
print("-----------------Tsdxed--------------------")
#prueba de Tsdxed
for p in dic:
    if len(p)==6:
        if p[0] in posT and p[1] in posS and p[2]==p[-1]:
            if p[3] in posX and p[4] in posE:
                c=c+1
                print(p)
print("----------------Fajg-----------------------")
#prueba con Fajg
for p in dic:
    if len(p)==4:
        if p[0] in posF and p[1] in posA:
            if p[2] in posJ and p[3] in posG:
                c=c+1
                print(p)
print("-----------------Lemvez--------------------")
#prueba con Lemvez
for p in dic:
    if len(p)==6:
        if p[0] in posL and p[2] in posM:
            if p[1]==p[4] and p[3] in posV:
                if p[-1] in posZ:
                    c=c+1
                    print(p)
print("-----------------Izsov---------------------")
#prueba con Izsov
for p in dic:
    if len(p)==5:
        if p[0] in posI and p[1] in posZ:
            if p[2] in posS and p[3] in posO:
                if p[-1] in posV:
                    c=c+1
                    print(p)
print("----------------xeoqküvrv-----------------")
#prueba de xeoqküvrv
for p in dic:
    if len(p)==9:
        if p[0] in posX and p[1] in posE and p[2] in posO:
            if p[3] in posQ and p[4] in posK and p[5] in posÜ:
                if p[6] in posV and p[7] in posR and p[-1] in posV:
                    c=c+1
                    print(p)

alfabeto = 'abcdefghijklmnopqrstuvwxyzäöüß'
llave_Al = 'XXvXeXXXXXXXXXXXqoXXkXXvXXXXüX'
b=descifraSustituye("z Fajg omvrv usg pey Kuto. Lemvez sdved omdp pme Izsov sdp pez Iusqk. Kmez omdp oekz cmete Azxude: pez Yuxed, pme Teiez, pme Dmezed, puo Kezr sdp pme Tsdxed sdp pez Puzy. Kezr sdp Tsdxe omdp cay Izsovfazi sdp ped Zmjjed xeoqküvrv.",llave_Al)
print(b)