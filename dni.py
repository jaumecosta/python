#funcion para la busqeuda de la letra del DNI
def letraDNI(dni):
    #conjunto de letras creado por la policia naciona
    listaLetras = 'TRWAGMYFPDXBNJZSQVHLCKEO'
    letra = listaLetras[dni%23]
    #busqeuda de la letra
    print(f'{dni}{letra}'.upper())
    #aumentar la letra .upper()
letraDNI(45184178)