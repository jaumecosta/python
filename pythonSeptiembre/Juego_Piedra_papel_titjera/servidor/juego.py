import os
import documentacion.opciones as juego
import random
import time
import arte

'''TONI VERSION INICIO'''


def ia():
    global resultado_ai
    resultado_ai = random.randint(0, 2)
    return arte.PIEDRA_PAPEL_TIJERA[resultado_ai]


def ganadores(usuario):
    if resultado_ai == usuario:
        resultado = 'EMPATE'
    else:
        if resultado_ai == 0 and usuario == 1:
            resultado = 'GANADOR'
        else:
            resultado = 'PERDEDOR'
        if resultado_ai == 0 and usuario == 1:
            resultado = 'GANADOR'
        else:
            resultado = 'PERDEDOR'
        if resultado_ai == 1 and usuario == 2:
            resultado = 'GANADOR'
        else:
            resultado = 'PERDEDOR'
        if resultado_ai == 2 and usuario == 0:
            resultado = 'GANADOR'
        else:
            resultado = 'PERDEDOR'

def escenario():
    os.system('clear')
    # responde el usuario
    print(arte.PIEDRA_PAPEL_TIJERA[usuario])
    print('tick, tack, tick, tack')
    time.sleep(3)
    # responder IA
    print(ia())
    # GANADOR
    print('?' * 50)
    print('RESULTADO DEL ENFRENTAMIENTO')
    print('?' * 50)
    time.sleep(1)
    print(ganadores(usuario))
    time.sleep(4)
def run():
    os.system('clear')
    global usuario
    usuario = int(input("""
        [0]Piedra
        [1]Tijera
        [2]Papel
    """))
    escenario()
'''TONI VERSION FIN'''

def pregunta(pregunta):
    if pregunta.upper() == "3":
        print(juego.Tijeras)
    if pregunta.upper() == "2":
        print(juego.Papel)
    if pregunta.upper() == "1":
        print(juego.Piedra)

# pregunta
os.system('clear')
print("[1]Piedra")
print("[2]Papel") 
print("[3]Tijeras")
jugador = input("Jugador1:Escoja una de las siguiente opciones:")
pregunta(jugador)
juegoDivertido = [juego.Tijeras, juego.Papel, juego.Piedra]  #Lista aleatorioa
fun = random.choice(juegoDivertido)
print('La maquina te quiere joder')
print(fun)

# JUGADOR
if jugador == juego.Piedra and fun == juego.Tijeras:
    print("Gana el jugador1")
elif jugador == juego.Tijeras and fun == juego.Papel:
    print("Gana el jugador1")
elif jugador == juego.Papel and fun == juego.Piedra:
    print("Gana el jugador1")
elif fun == juego.Piedra and jugador == juego.Tijeras:
    print("Gana la puta maquina, viva SKYNET")
elif fun == juego.Tijeras and jugador == juego.Papel:
    print("Gana la puta maquina, viva SKYNET")
elif fun == juego.Papel and jugador == juego.Piedra:
    print("Gana la puta maquina, viva SKYNET")
else:
    ('EMPATE A REPETIR')
