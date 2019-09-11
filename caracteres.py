# detectar cual es el primer caracter que no se repite, la cadena de caracteres se pone mediante un input
# [jcbjde]

    #resultado caracter(letra)
#funciones
'''

    print('DESCUBRE CUAL ES EL CARACTER QUE NO SE REPITE')
    print('ESVRIBE EL CADENA DE CARACTERES')
    #letra = str(input('Introduce una cadena de texto:'))
    lista = ['j','c','b','j','e','d']
    lista.append()
    print(lista)
    if letra == lista:
        return True
    else:
        return False
'''
def primer_caracter_NO_repite(secuencia):
    for i in secuencia:
        if secuencia.count(i) > 1:
            continue
        else:
            return i

    return False

if __name__ == "__main__":
    secuencia = 'jcbjed'
    resultado = primer_caracter_NO_repite(secuencia)
    if resultado == False:
        print('Todos los caracteres de la cadena se repiten')
    else:
        print(f'El primer caracte no repetido es:{resultado}')