def cargaPalabras():
    archivo = open('Frances.txt', 'r')
    renglon = archivo.readline()
    palabras = renglon.split()
    print (len(palabras), 'palabras leidas')
    return palabras

def descifraSustituye(cadena, alfabetoLlave,alfabeto):
    nuevaCadena = ""
    for letra in cadena:
        if letra in alfabetoLlave:
            posicion = alfabetoLlave.find(letra)
            nuevaCadena = nuevaCadena + alfabeto[posicion]
        else:
            nuevaCadena = nuevaCadena + letra
    return nuevaCadena

texto_cifrado='Zx rnplibbi zxvanr Gi lvira s’izzirxhiq sxra zx rnplibbi zxvanr. Ibbi iae ybpa gnbvi mpi kibbi mpi g’xlxva xlxre. Zx rnplibbi zxvanr iae obxrkui xlik sia lnbiea obipa ie sia tbipqa qnphia. G’xv pr hxqxhi ynpq zx lnvepqi ie ynpq znr libn. X b’vreiqvipq si zx zxvanr, vb j x pr hqxrs axbnr xlik pri exobi ie mpxeqi kuxvaia ynpq xkkpivbbvq zia xzva. Znr kuxe xsnqi ai obneevq apq bi kxrxyi silxre bx eibilvavnr. Bx kpvavri iae bx yviki yqitiqii si zx zxvanr. K’iae vkv mpi gi kpvavri sia hxeixpf ie sia yxevaaiqvia. Ynpq xbbiq sxra zx kuxzoqi, gi snva znreiq pr iakxbviq. Ibbi ai avepi xp onpe sp knpbnvq, x sqnvei. G’xv sikvsi si yivrsqi bia zpqa ir gxpri ie s’j vraexbbiq znr yvxrn. X hxpkui, k’iae zx axbbi si oxvr, xlik lpi apq znr gxqsvr. Gi zi aira eqia ovir sxra zx rnplibbi zxvanr!'.lower()

#3 letras no van a estar
alfabeto = 'abcdefghijklmnopqrstuvwxyz'  
llave_fr = 'xoksithuvgXbzrnymqaeplXXjf'
print(texto_cifrado)
b=descifraSustituye(texto_cifrado,llave_fr,alfabeto)
print(b)
