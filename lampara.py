# 1 encender
#0 apagagar

import os
import random
class Lampara():
    _LAMPARA = [
   '''
       .----------.
       |   ON     |
       |   ____   |
       |  |.--.|  |
       |  ||  ||  |
       |  ||__||  |
       |  ||\ \|  |
       |  |\ \_\  |
       |  |_\[0]  |
       |          |
       |  OFF     |
       ‘----------’
       ''',
       '''
       .----------.
       |   ON     |
       |   __     |
       |  | /[0]  |
       |  |/ / /  |
       |  ||/_/|  |
       |  ||  ||  |
       |  ||  ||  |
       |  |.__.|  |
       |          |
       |  OFF     |
       ‘----------’
       '''
    ]


#Metodos
    def __init__(self,se_encendera):
        self.se_encendera = se_encendera

    def encender(self):
        self.se_encendera = True
        self.__llamar_imagen()
    
    def apagar(self):
        self.se_encendera = False
        self.__llamar_imagen()

    
    def __llamar_imagen(self):
        if (self.se_encendera):
            print(f'{self._LAMPARA[1]}\x1b[1;32m')
        else:
            print(f'{self._LAMPARA[0]}\x1b[1;31m')
    def fundido(self):
        #bucle bomba
        while True
       self.se_encendera = True
        if (self.):
           print('ALLAHU AKCBAR')
#funcion
def iniciar(self):
    os.system('clear')
    interruptor = Lampara(se_encendera = True)

    while True:
        if interruptor.fundido == True:
            print('allahu akcbar')
            break
        pregunta = int(input('''\x1b[1;32m
            Seleccina una opcion:
            [1]Encender
            [0]Apagar
            [2]Salir
        '''))
        if pregunta == 1 and interruptor.se_encendera == False:
            interruptor.cont += 1
            print(f'{interruptor.encender()}\x1b[1;32m')
        elif pregunta == 0 and interruptor.se_encendera == True:
            print(f'{interruptor.apagar()}\x1b[1;31m')
        elif pregunta == 1 or pregunta == 0:
            print('Eres mongolo')
        else:
            break
       #· while True:
        #    if interruptor.encender() > 4:
        #        print('allahu akcbar')
        #    break
     #   if interruptor.encender() > 4:
#inicio de progrma
if __name__ == "__main__":
    iniciar()




'''
       
class Lampara():
    def __init__(self):
        self.__encendido == 1
        self.__apagado == 0
     
    def __encendidoLampara(self):
        print('Hay que encender la puta lampara')
        boton = int(input('Pona 1  si quiere la lampara encendida o 0 para la lampara apagada'))
        self.activo = True
        self.inactivo = False
        if (self.activo):
            return True
        else:
            return False

        if (self.encendido and boton == 1):
            print('Lampara encendida')
        else:
            print('Lampara apagada')            
      
print('-------------------------INSTANCIA DEL OBJETO--------------------------')

print(boton.encendidoLampara(True))
boton.__encendidoLampara()

                
'''