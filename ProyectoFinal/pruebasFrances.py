def cargaPalabras():
    archivo = open('Frances.txt', 'r')
    renglon = archivo.readline()
    palabras = renglon.split()
    print (len(palabras), 'palabras leidas')
    return palabras

def descifraSustituye(cadena, alfabetoLlave,alfabeto):
    nuevaCadena = ""
    for letra in cadena:
        if letra in alfabeto:
            posicion = alfabetoLlave.find(letra)
            nuevaCadena = nuevaCadena + alfabeto[posicion]
        else:
            nuevaCadena = nuevaCadena + letra
    return nuevaCadena

texto_cifrado='Zx rnplibbi zxvanr Gi lvira s’izzirxhiq sxra zx rnplibbi zxvanr. Ibbi iae ybpa gnbvi mpi kibbi mpi g’xlxva xlxre. Zx rnplibbi zxvanr iae obxrkui xlik sia lnbiea obipa ie sia tbipqa qnphia. G’xv pr hxqxhi ynpq zx lnvepqi ie ynpq znr libn. X b’vreiqvipq si zx zxvanr, vb j x pr hqxrs axbnr xlik pri exobi ie mpxeqi kuxvaia ynpq xkkpivbbvq zia xzva. Znr kuxe xsnqi ai obneevq apq bi kxrxyi silxre bx eibilvavnr. Bx kpvavri iae bx yviki yqitiqii si zx zxvanr. K’iae vkv mpi gi kpvavri sia hxeixpf ie sia yxevaaiqvia. Ynpq xbbiq sxra zx kuxzoqi, gi snva znreiq pr iakxbviq. Ibbi ai avepi xp onpe sp knpbnvq, x sqnvei. G’xv sikvsi si yivrsqi bia zpqa ir gxpri ie s’j vraexbbiq znr yvxrn. X hxpkui, k’iae zx axbbi si oxvr, xlik lpi apq znr gxqsvr. Gi zi aira eqia ovir sxra zx rnplibbi zxvanr!'.lower()
dic = cargaPalabras()

posA='abcdefghijklmnopqrstuvwxyz'
posB='abcdefghijklmnopqrstuvwxyz'
posE='abcdefghijklmnopqrstuvwxyz'
posF='abcdefghijklmnopqrstuvwxyz'
posG='abcdefghijklmnopqrstuvwxyz'
posH='abcdefghijklmnopqrstuvwxyz'
posI='abcdefghijklmnopqrstuvwxyz'
posJ='abcdefghijklmnopqrstuvwxyz'
posK='abcdefghijklmnopqrstuvwxyz'
posL='abcdefghijklmnopqrstuvwxyz'
posM='abcdefghijklmnopqrstuvwxyz'
posN='abcdefghijklmnopqrstuvwxyz'
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

print("--------------------kibbi---------------")
#prueba con kibbi
for p in dic:
    if len(p)==5:
        if p[1]==p[-1] and p[2]==p[3]:
            if p[0] in posK:
                c=c+1
                print(p)
print("--------------------si--------------------")
#prueba con si
for p in dic:
    if len(p)==2:
        if p[0] in posS and p[1] in posI:
            c=c+1
            print(p)
print("-------------------axbbi-------------------")
#prueba con axbbi
for p in dic:
    if len(p)==5:
        if p[2]==p[3]:
            if p[0] in posA and p[1] in posX and p[-1] in posI:
                c=c+1
                print(p)
print("---------------------Gi---------------------")
#prueba con Gi
for p in dic:
    if len(p)==2:
        if p[0] in posG and p[-1] in posI:
            c=c+1
            print(p)
print("-----------------------zi-------------------")
#prueba con zi
for p in dic:
    if len(p)==2:
        if p[0] in posZ and p[-1] in posI:
            c=c+1
            print(p)
print("---------------------sxra------------------")
#prueba con sxra
for p in dic:
    if len(p)==4:
        if p[0] in posS and p[1] in posX:
            if p[2] in posR and p[-1] in posA:
                c=c+1
                print(p)
print("-----------------------qnphia----------------")
#prueba con qnphia
for p in dic:
    if len(p)==6:
        if p[0] in posQ and p[1] in posN:
            if p[2] in posP and p[3] in posH:
                if p[4] in posI and p[-1] in posA:
                    c=c+1
                    print(p)
print("---------------------obipa-------------------")
#prueba con obipa
for p in dic:
    if len(p)==5:
        if p[0] in posO and p[1] in posB:
            if p[2] in posI and p[3] in posP and p[-1] in posA:
                c=c+1
                print(p)
print("------------------Zx------------------")
#prueba con Zx
for p in dic:
    if len(p)==2:
        if p[0] in posZ and p[-1] in posX:
            c=c+1
            print(p)
print("-------------------------s’j-----------------")
#prueba con s’j
for p in dic:
    if len(p)==2:
        if p[0] in posS and p[-1] in posJ:
            c=c+1
            print(p)
print("------------------------exobi------------------")
#prueba con exobi
for p in dic:
    if len(p)==5:
        if p[0] in posE and p[1] in posX:
            if p[2] in posO and p[3] in posB and p[-1] in posI:
                c=c+1
                print(p)
print("---------------------------hxeixpf--------------")
#prueba con hxeixpf
for p in dic:
    if len(p)==7:
        if p[1]==p[4] and p[0] in posH:
            if p[2] in posE and p[3] in posI:
                if p[5] in posP and p[-1] in posF:
                    c=c+1
                    print(p)
print("----------------------------Bx---------------")
#prueba con Bx
for p in dic:
    if len(p)==2:
        if p[0] in posB and p[-1] in posX:
            c=c+1
            print(p)
print("----------------------zpqa----------------")
#prueba con zpqa
for p in dic:
    if len(p)==4:
        if p[0] in posZ and p[1] in posP:
            if p[2] in posQ and p[-1] in posA:
                c=c+1
                print(p)
print("--------------------ovir-------------------")
#prueba con ovir
for p in dic:
    if len(p)==4:
        if p[0] in posO and p[1] in posV:
            if p[2] in posI and p[-1] in posR:
                c=c+1
                print(p)
print("-----------------------Ynpq-------------------")
#prueba con Ynpq
for p in dic:
    if len(p)==4:
        if p[0] in posY and p[1] in posN:
            if p[2] in posP and p[-1] in posQ:
                c=c+1
                print(p)
print("-----------------------G’xv---------------")
#prueba con G’xv
for p in dic:
    if len(p)==3:
        if p[0] in posG and p[1] in posX and p[-1] in posV:
            c=c+1
            print(p)
print("-----------------------hqxrs--------------")
#prueba con hqxrs
for p in dic:
    if len(p)==5:
        if p[0] in posH and p[1] in posQ and p[2] in posX:
            if p[3] in posR and p[-1] in posS:
                c=c+1
                print(p)
print("----------------------pri-----------------")
#prueba con pri
for p in dic:
    if len(p)==3:
        if p[0] in posP and p[1] in posR and p[-1] in posI:
            c=c+1
            print(p)
print("---------------------pr-------------------")
#prueba con pr
for p in dic:
    if len(p)==2:
        if p[0] in posP and p[-1] in posR:
            c=c+1
            print(p)
print("-----------------------ie---------------")
#prueba con ie
for p in dic:
    if len(p)==2:
        if p[0] in posI and p[-1] in posE:
            c=c+1
            print(p)

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
llave_fr = 'xoksithuvgXbzrnymqaeplXXjf'
print(texto_cifrado)
b=descifraSustituye(texto_cifrado,llave_fr,alfabeto)
print(b)
