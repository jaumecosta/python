#10 a 20 adivinar numero aleatorio
 #elegir partida de 10(5) 25(10) vidas o 50(20) vidas
import random
import os

def inicio():
    os.system('clear')

    encontrar_numero = False
    numero_aleatorio = random.randint(0, 20)

    while not encontrar_numero:
        numero = int(input('Intenta adivinar tu numero ganador: '))

        if numero == numero_aleatorio:
            print('Felicidades, has ganado un chupa-chup')
            encontrar_numero = True
        elif numero > numero_aleatorio:
            print('El número es más pequeño')
        else:
            print('El numero es más grande')
            
if __name__ == "__main__":
    inicio()
    '''
print('A D I V I N A  E L  N U M E R O')
print('-------------------------------')
contador = 0
    for i in bucle:
         numero = int(input("ADIVINA EL NUMERO:"))

    if(aleatorio == numero):
        print("ACERTASTE")
    else:
        print("TE EQUIVOCASTE")


    '''