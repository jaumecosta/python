# 10 a 20 adivinar numero aleatorio
# elegir partida de 10(5) 25(10) vidas o 50(20) vidas
import random
import os


def eleccion_juego():
    print('ELIJA LA PARTIDA DE DESEA JUGAR')
    print('Si quiere un partida de 10 con 5 vidas ponga 1')
    print('Si quiere un partida de 25 con 10 vidas ponga 2')
    print('Si quiere un partida de 50 con 20 vidas ponga 3')
    numero = int(input('ELIGA LA PARTIDA:'))
    if numero == 1:
        partida1()
    elif numero == 2:
        partida2()
    elif numero == 3:
        partida3()
    else:
        print('ERROR')

def inicio():

    encontrar_numero = False
    numero_aleatorio = random.randint(0, numero_aleatorio)
    while not encontrar_numero:
        numero = int(input('Intenta adivinar tu numero ganador: '))

        if numero == numero_aleatorio:
            print('Felicidades, has ganado un chupa-chup')
            encontrar_numero = True
        elif numero > numero_aleatorio:
            print('El número es más pequeño')
        else:
            print('El numero es más grande')


def partida1():
    os.system('clear')

    numero_aleatorio = random.randint(0, 10)

def partida2():
    os.system('clear')

    numero_aleatorio = random.randint(0, 25)

def partida3():
    os.system('clear')

    numero_aleatorio = random.randint(0, 50)


if __name__ == "__main__":
    partida1()
    partida2()
    partida3()


    eleccion_juego()
