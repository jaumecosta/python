import os
​import random

from clases import Lampara

# función
def iniciar():
​
    interruptor = Lampara(se_encendera = True)
​
    interruptor.estado()

    while True:
        if (interruptor.fundir(fundifo = True) == False):

        pregunta = int(input('''
            Selecciona una opción:
            [1] Encender
            [0] Apagar
            [2] Salir
        '''))
​
        if pregunta == 1:
            cont += 1
            print(interruptor.encender())
        elif pregunta == 0:
            print(interruptor.apagar())
        else:
            break
​
​
# inicio de programa
if __name__ == "__main__":
    iniciar()