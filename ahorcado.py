import random
palabras = ['TORTUGA', 'PEZ', 'MONO', 'PERRO', 'MURCIELAGO', 'JIRAFA', 'ELEFANTE']
sprites = [
    '''
    *---*
    |   |
        |
        |
        |
        |
        *=======*
'''
    ,
    '''
    *---*
    |   |
    O   |
        |
        |
        |
        *=======*
'''
    ,
    '''
    *---*
    |   |
    O   |
    |   |
    |   |
        |
        *=======*
'''
    ,
    '''
    *---*
    |   |
    O   |
   /|   |
    |   |
        |
        *=======*
'''
    ,
    '''
    *---*
    |   |
    O   |
   /|\  |
    |   |
        |
        *=======*
'''
    ,
    '''
    *---*
    |   |
    O   |
   /|\  |
    |   |
   /    |
        *=======*
'''
    ,
    '''
    *---*
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        *=======*
'''
]
def palabra_aleatoria():
    numero_random = random.randint(0, len(palabras) - 1)
    palabra_oculta = str(palabras[numero_random])
    return palabra_oculta
def tablero(ocultar, intentos):
    print(sprites[intentos])
    print('')
    print(ocultar)
def inicio():
    palabraOK = palabra_aleatoria()
    numero_letras = len(palabraOK)
    ocultar = ['_'] * numero_letras
    intentos = 0
    while True:
        print('')
        tablero(ocultar, intentos)
        letra = str(input('Introduce una letra: '))
        indexarLetra = []
        for i in range(len(palabraOK)):
            if palabraOK[i] == letra:
                indexarLetra.append(i)
                print(indexarLetra)
        if len(indexarLetra) == 0:
            intentos += 1
        # Perder
        if intentos == 7:
            print('')
            print(f'T H E  E N D')
            print(f'La palabra correcta es {palabraOK}')
            break
        else:
            for i in indexarLetra:
                ocultar[i] = letra
                indexarLetra = [i]
if __name__ == "__main__":
    inicio()