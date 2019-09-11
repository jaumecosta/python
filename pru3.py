'''
POO en python
'''


class Clase():

    def __init__(self):
        self.cosa = False  # inicio variable constructor


class Coche():  # CONSTRUCTOR
    # Estadp Inicial bajo un constructor
    def __init__(self):  # constructor
        self.__largoChasis = 200
        self.__anchoClase = 99
        self.__ruedas = 4  # encapsular ruedas
        self.__enMarcha = False

    # Crear un metodo   METODOS

    def __chequeoArranque(self):
        print('Estamos realizando el chequeo de puesta en marcha')

        self.gasolina = True
        self.aceite = True
        self.puertasCerradas = True
        self.bateria = True

        if (self.gasolina and self.aceite and self.puertasCerradas and self.bateria):
            return True
        else:
            return Fals

    if (self.enMarcha and chequeo):
            return 'El coche esta en marcha'
    elif (self.enMarcha and chequeo == False):
            return 'Problemas al arrancar'
    else:
            return 'El coche esta parado'




    def arrancar(self, arrancamos):
        self.enMarcha = arrancamos

        if (self.enMarcha):
        chequeo = self.__chequeo

        if (self.arrancar):
            return 'El coche esta en marcha'
        else:
            return 'El coche esta parado'




    def estado(self):
        print(f'El coche tiene{self.ruedas} ruedas, un ancho de {self.anchoChasis} y un largo de {self.largoChasis}')
# Instanciar una clase. Crear un objeto
# No se utiliza new
miCoche = Coche()
print(miCoche.arrancar(True))

miCoche.estado()
print('-----------------------------Segunda Instancia Objeto-------------------------------')

cocheDelVecino = Coche()

print(miCoche.arrancar(True))


miCoche.estado()


print('-----------------------------Tercera Instancia Objeto-------------------------------')

camion = Coche()

print(miCoche.arrancar(False))
'''
# Acceder a las propiedades
print(miCoche.arrancar(True))

# Acceder a los metodos
miCoche.estado()
'''
