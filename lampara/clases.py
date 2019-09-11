import os
import random
class Lampara():

#clase lampara
    from asciiArt import _LAMPARA
 
    cont = 0
    fundido = False
    # Métodos
    def __init__(self,se_encendera):
        self.se_encendera = se_encendera
              
    def estado(self):
        pulsar = random.randint(0, 1)
        if (pulsar == 0):
            print(f'\x1b[1;30m {self._LAMPARA[pulsar]}')
            self.se_encendera = False
        else:
            print(f'\x1b[1;31m {self._LAMPARA[pulsar]}')
            self.se_encendera = True



    def encender(self):
        self.se_encendera = True
        
        self.__llamar_imagen()
​
    def apagar(self):
        self.se_encendera = False
        self.__llamar_imagen()
​
    def __llamar_imagen(self):
        if (self.se_encendera):
            print(self._LAMPARA[1])
        else:
            print(self._LAMPARA[0])
​
    def fundir(self):
        pass
    
​