'''palindromo '''

def palindromo(palabra):
    palabraInvertida = palabra[::-1]  #INVIERTE CONTENIDO
    if palabraInvertida == palabra:
        return True
    else:
        return False
#OTRA OPCION

#funciones
def inicio():
    print('F R I K I S  D E  L O  P A L I N D R O M O S')
    print('-------------------------------------------')
    print('')
    
    palabra = str(input('Introduce una palabra:'))

    resultado = palindromo(palabra)

    if resultado == True:
        print('Es un palindromo')
    else:
        print('No es palindromo')
    



if __name__ == "__main__":
    inicio()


