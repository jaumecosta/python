
import random

def busquedaBinaria(numeros, encontrarNumero, bajo, alto):
    if bajo > alto:
        return False

    #resultado 3
    medio = int((bajo + alto) / 2)

    # 9 0 12 false
    if numeros[medio] == encontrarNumero:
        return True
    # 9 > 12 False
    elif numeros[medio] > encontrarNumero:
        return busquedaBinaria(numeros, encontrarNumero, bajo, medio -1)

    else:
        return busquedaBinaria(numeros, encontrarNumero, medio + 1, alto)

    #inicio
if __name__ == "__main__":
    #Lista aleatoria sin repeticiones
    numeros = [1,4,7,9,13,45,78,90]

    #numero a buscar
    encontrarNumero = int(input('Ingresar numero: '))

    # return de la funcion (false o True)
    resultado = busquedaBinaria(numeros, encontrarNumero, 0, len(numeros) -1)

    #Soulcion
    if resultado is True:
        print('El numero si esta en la lista')
    else:
        print('El numero NO esta en la lista')