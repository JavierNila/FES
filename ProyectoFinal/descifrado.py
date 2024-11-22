def cargaCifrado(nombreArchivo):
    txt = nombreArchivo + '.txt'
    archivo = open(txt,'r')
    renglon = archivo.readline()
    return renglon

def descifraSustituye(alfabeto ,cadena, alfabetoLlave):
    alfabeto = ''
    nuevaCadena = ""
    for letra in cadena:
        if letra in alfabeto:
            posicion = alfabetoLlave.find(letra)
            nuevaCadena = nuevaCadena + alfabeto[posicion]
        else:
            nuevaCadena = nuevaCadena + letra
    return nuevaCadena

def letrasDeTexto(alfabeto, historial, cifrado):
    for letra in cifrado:
        if letra in alfabeto:
            historial[letra] += 1
    return historial

if __name__ == '__main__':
    cifrado_Aleman = "z Fajg omvrv usg pey Kuto. Lemvez sdved omdp pme Izsov sdp pez Iusqk. Kmez omdp oekz cmete Azxude: pez Yuxed, pme Teiez, pme Dmezed, puo Kezr sdp pme Tsdxed sdp pez Puzy. Kezr sdp Tsdxe omdp cay Izsovfazi sdp ped Zmjjed xeoqküvrv.".lower()
    historial_Aleman = {}
    alfabeto_aleman = "abcdefghijklmnopqrstuvwxyzäöüß"
    llave_Aleman = ""

    cifrado_Frances = "Zx rnplibbi zxvanr Gi lvira s’izzirxhiq sxra zx rnplibbi zxvanr. Ibbi iae ybpa gnbvi mpi kibbi mpi g’xlxva xlxre. Zx rnplibbi zxvanr iae obxrkui xlik sia lnbiea obipa ie sia tbipqa qnphia. G’xv pr hxqxhi ynpq zx lnvepqi ie ynpq znr libn. X b’vreiqvipq si zx zxvanr, vb j x pr hqxrs axbnr xlik pri exobi ie mpxeqi kuxvaia ynpq xkkpivbbvq zia xzva. Znr kuxe xsnqi ai obneevq apq bi kxrxyi silxre bx eibilvavnr. Bx kpvavri iae bx yviki yqitiqii si zx zxvanr. K’iae vkv mpi gi kpvavri sia hxeixpf ie sia yxevaaiqvia. Ynpq xbbiq sxra zx kuxzoqi, gi snva znreiq pr iakxbviq. Ibbi ai avepi xp onpe sp knpbnvq, x sqnvei. G’xv sikvsi si yivrsqi bia zpqa ir gxpri ie s’j vraexbbiq znr yvxrn. X hxpkui, k’iae zx axbbi si oxvr, xlik lpi apq znr gxqsvr. Gi zi aira eqia ovir sxra zx rnplibbi zxvanr !".lower()
    historial_Frances = {}
    alfabeto_frances = "abcdefghijklmnopqrstuvwxyz"
    llave_Frances = "xoksithuvgXbzrnymqaeplXXjf"

    for e in alfabeto_aleman:
        historial_Aleman[e] = 0

    for e in alfabeto_frances:
        historial_Frances[e] = 0

    print(letrasDeTexto(alfabeto_aleman, historial_Aleman, cifrado_Aleman))
    print(letrasDeTexto(alfabeto_frances, historial_Frances, cifrado_Frances))

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
llave_fr = 'xoksithuvgXbzrnymqaeplXXjf'
print(cifrado_Frances)
b=descifraSustituye(cifrado_Frances,llave_fr,alfabeto)
print(b)
